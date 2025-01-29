"""
URL configuration for LibraryManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# import include & re_path
from django.urls import path, include, re_path

##################################################################

# add a path to the app urls
# match URLs starting with 'api/' followed by version
# - capture 'v1' & store it in the parameter called 'version'
# - needed for URLPathVersioning to ID API version
# https://www.django-rest-framework.org/api-guide/versioning/#urlpathversioning
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/(?P<version>(v1))/', include('LibraryAPI.urls')), # have to explicitly define which versions are allowed
]
