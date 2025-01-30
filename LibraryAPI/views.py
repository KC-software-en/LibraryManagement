from django.shortcuts import render

# import ModelViewSet for CRUD operationss containing minimal code
from rest_framework.viewsets import ModelViewSet

# import Response to return API responses in correct format
from rest_framework.response import Response

# import status for HTTP status codes
from rest_framework import status

# import models
from .models import Book

# import serializers
from .serializers import BookSerializer

# import utils functions
from .utils import fetch_rate_limit_info

# import NotFound for book endpoints that do not exist
from rest_framework.exceptions import NotFound

# import error for when a book ID endpoint does not exist
from django.http import Http404

########################################################################

# Create your views here.

# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(),
# and instead provides actions such as .list() and .create()
# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
# register the viewset with a router class, that automatically determines the urlconf
class BookViewSet(ModelViewSet):
    # define a queryset that allows access to all Book objects using all() method
    queryset = Book.objects.all()
    # specify the serializer class for this viewset
    serializer_class = BookSerializer

    # override the get_object to customise 404 handling
    # - it enables error response formatting in the retrieve() method
    def get_object(self):
        try:
            # try to get the object using parent class's get_object method
            return super().get_object()
        
        except Http404:
            # raise django's exception if the object was not found
            raise NotFound()    

    # override the list method to handle GET requests with a custom message
    def list(self, request, *args, **kwargs):
        # get the queryset of all Book objects
        queryset = self.get_queryset()

        # check if queryset is empty and provide a message
        # use 200 status instead of 204 since there was a successful request & a message in the Response
        # call utils function to fetch rate limit info
        if not queryset.exists():
            return Response(
                {"status": "success",
                "code": 200,
                "message": "There are no Books in the library",
                "data": [],
                "headers": fetch_rate_limit_info(request, self),
                },
                status=status.HTTP_200_OK,
                )

        # serialize the queryset using the serializer class
        serializer = self.get_serializer(queryset, many=True)
        # return a response with the serialized data
        return Response(
            {
                "status": "success",
                "code": 200,
                "message": "Successfully retrieved all Books",
                "data": serializer.data,
                "headers": fetch_rate_limit_info(request, self),
            },
            status=status.HTTP_200_OK,
            )
    
    # override the retrieve method to handle GET requests with a custom message
    def retrieve(self, request, *args, **kwargs):
        # use defensive programming with try-except blocks
        try:
            # get the book instance to be retrieved
            instance = self.get_object()
            # serialize the book instance using the serializer class
            serializer = self.get_serializer(instance)

            # return a response with the serialized data
            # call utils function to fetch rate limit info
            return Response(
                {
                    "status": "success",
                    "code": 200,
                    "message": "Successfully retrieved Book",
                    "data": serializer.data,
                    "headers": fetch_rate_limit_info(request, self),
                },
                status=status.HTTP_200_OK,
                )
        
        except NotFound:
            # return a response with a message if the book does not exist
            # call utils function to fetch rate limit info
            return Response(
                {
                    "status": "error",
                    "code": 404,
                    "message": "No Book matches the given query",
                    "data": None,
                    "headers": fetch_rate_limit_info(request, self),
                },
                status=status.HTTP_404_NOT_FOUND,
                )
    
    # override the create method to handle POST requests with a custom message
    def create(self, request, *args, **kwargs):
        # get the data from the request
        data = request.data

        # create a new book instance using the serializer
        # the serializer will validate the data and create a new book object
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # save the new book object to the database
        self.perform_create(serializer)
        # return a response with the serialized data and a 201 status code
        headers = self.get_success_headers(serializer.data)

        # return a response with a message if the book was created
        # call utils function to fetch rate limit info
        return Response(
            {
                "status": "success",
                "code": 201,
                "message": "Successfully added Book",
                "data": serializer.data,
                "headers": fetch_rate_limit_info(request, self),
            },            
            status=status.HTTP_201_CREATED, 
            # return headers since the generic modelviewset is was overwritten
            # this will help clients locate the newly created resource; maintains good REST practices
            headers=headers,
            )

    # override the update method to handle PUT requests with a custom message
    # PUT replaces existing resource, ensuring sending the same data does not create duplicates
    # - DRF validates incoming request against the serializer, preventing unintended updates
    # - thus idempotent: the response is consistent for the same request sent multiple times
    def update(self, request, *args, **kwargs):
        # determine if the client wants a full (PUT) or partial (PATCH) update
        # partial will be True for PATCH and False for PUT
        partial =  kwargs.pop('partial', False)
        # get the book instance to be updated
        instance = self.get_object()
        # get the data from the request
        data = request.data

        # update the book instance using the serializer
        # the serializer will validate the data and update the book object
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # save the updated book object to the database
        self.perform_update(serializer)
        # return a response with the serialized data and a 201 status code
        headers = self.get_success_headers(serializer.data)
        
        # return a response with the serialized data
        # call utils function to fetch rate limit info
        return Response(
            {
                "status": "success",
                "code": 200,
                "message": "Successfully updated Book",
                "data": serializer.data,
                "headers": fetch_rate_limit_info(request, self),
            }, 
            status=status.HTTP_200_OK,
            # return headers since the generic modelviewset is was overwritten
            # this will help clients locate the newly created resource; maintains good REST practices
            headers=headers,
            )
    
    # override the destroy method to handle DELETE requests with a custom message
    def destroy(self, request, *args, **kwargs):
        # get the book instance to be deleted
        instance = self.get_object()
        # delete the book object from the database
        self.perform_destroy(instance)
        
        # return a response with a 204 status code
        # call utils function to fetch rate limit info
        return Response(
            {
                "status": "success",
                "code": 204,
                "message": "Successfully deleted Book",
                "headers": fetch_rate_limit_info(request, self),
            },
            status=status.HTTP_204_NO_CONTENT,
            )

