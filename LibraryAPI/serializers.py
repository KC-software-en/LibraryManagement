# import serializers to convert complex datatypes like django model to pyhton datatypes that can be easily rendered in JSON, XML, etc
from rest_framework import serializers

# import Book model from the current directory
from .models import Book

# import validators from django
from django.core.validators import MinLengthValidator

# import date
from datetime import date

#########################################################################################################

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

        # ensure all fields are required when creating a new book with POST
        extra_kwargs = {
            field: {"required": True} for field in fields
            }

        # validate that the author & title combination is unique
        # https://www.django-rest-framework.org/api-guide/validators/#uniquetogethervalidator
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['title', 'author'],
                message="This book by this author already exists."
            )
        ]

    # validate title field
    title = serializers.CharField(
        validators=[MinLengthValidator(1, message="Title must be at least 1 character long.")]
    )

    # validate author field
    author = serializers.CharField(
        validators=[MinLengthValidator(2, message="Author must be at least 2 characters long.")]
    )

    # validate genre field
    genre = serializers.CharField(
        validators=[MinLengthValidator(3, message="Genre must be at least 3 characters long.")]
    )

    # validate summary field
    summary = serializers.CharField(
        validators=[MinLengthValidator(10, message="Summary must be at least 10 characters long.")]
    )

    # validate published date field   
    # https://www.django-rest-framework.org/api-guide/validators/#function-based 
    def validate_published_date(self, value): # method is called when checking if serializer is valid in views.py
        if value > date.today():
            raise serializers.ValidationError("Published date must be before or equal to today's date.")
        return value