# import timezone
from django.utils import timezone

# import datetime
from datetime import datetime, timedelta

# import cache
from django.core.cache import cache

###################################################################

# define a function to retrieve rate limit information
# use view as the parameter to access throttle class configured for that view
# - to generate the correct cach key
# - & maintain consistency with DRF's internal patterns
def fetch_rate_limit_info(request, view):
    # get 1st throttle class instance from the view's throttle_classes list
    throttle = view.throttle_classes[0]()

    # check if throttle has a rate attribute (i.e. 100/hour) else none was configured
    if not hasattr(throttle, 'rate'):
        return None
    
    # parse rate limit details
    num_of_requests, duration = throttle.parse_rate(throttle.rate)

    # get the current user's request history
    key = throttle.get_cache_key(request, view)
    history = cache.get(key, [])

    # get the current timestamp
    now = timezone.now()
    now_ts = now.timestamp()

    # clean old history - compare timestamps instead of datetime objects
    while history and history[-1] <= now_ts - duration:
        history.pop()

    # add current timestamp to history
    history.insert(0, now_ts)

    # save updated history to cache
    cache.set(key, history, duration)

    # calculate remaining requests
    remaining_requests = max(num_of_requests - len(history), 0)

    # calculate reset time
    reset_time = int(now_ts + duration)

    # return the rate limit information 
    return {
        "X-RateLimit-Limit": num_of_requests,
        "X-RateLimit-Remaining": remaining_requests,
        "X-RateLimit-Reset": reset_time
    }
