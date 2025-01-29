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

########################################################################

# Create your views here.

# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(),
# and instead provides actions such as .list() and .create()
# bind actions when finalising view, using the .as_view() method
# register the viewset with a router class, that automatically determines the urlconf
class BookViewSet(ModelViewSet):
    # define a queryset that allows access to all Book objects using all() method
    queryset = Book.objects.all()
    # specify the serializer class for this viewset
    serializer_class = BookSerializer

    # override the list method to handle GET requests with a custom message
    def list(self, request, *args, **kwargs):
        # get the queryset of all Book objects
        queryset = self.get_queryset()
        # serialize the queryset using the serializer class
        serializer = self.get_serializer(queryset, many=True)
        # return a response with the serialized data
        return Response(
            {
                "status": "success",
                "code": 200,
                "message": "Successfully retrieved all Books",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
            )
    
    # override the retrieve method to handle GET requests with a custom message
    def retrieve(self, request, *args, **kwargs):
        # get the book instance to be retrieved
        instance = self.get_object()
        # serialize the book instance using the serializer class
        serializer = self.get_serializer(instance)
        # return a response with the serialized data
        return Response(
            {
                "status": "success",
                "code": 200,
                "message": "Successfully retrieved Book",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
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
        return Response(
            {
                "status": "success",
                "code": 201,
                "message": "Successfully added Book",
                "data": serializer.data,
            },            
            status=status.HTTP_201_CREATED, 
            # return headers since the generic modelviewset is was overwritten
            # this will help clients locate the newly created resource; maintains good REST practices
            headers=headers,
            )

    # override the update method to handle PUT requests with a custom message
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
        return Response(
            {
                "status": "success",
                "code": 200,
                "message": "Successfully updated Book",
                "data": serializer.data,
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
        return Response(
            {
                "status": "success",
                "code": 204,
                "message": "Successfully deleted Book",
            },
            status=status.HTTP_204_NO_CONTENT,
            )

