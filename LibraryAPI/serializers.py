# import serializers to convert complex datatypes like django model to pyhton datatypes that can be easily rendered in JSON, XML, etc
from rest_framework import serializers

# import Book model from the current directory
from .models import Book

# define a serializer class  for the book model that inherits from ModelSerializer
# ModelSerializer automaticallycreates a set of fields & default validators based on the model 
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class BookSerializer(serializers.ModelSerializer):
    # use a meta class to provide metadata to the ModelSerializer
    # specify the book model
    # include all fields
    class Meta:
        model = Book
        fields = '__all__'    