import re, datetime
from django.conf import settings
from rest_framework import serializers
from .models import Book, BorrowedBook
from authapp.models import LibararyUser


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""
    class Meta:
        model = Book
        fields = "__all__"
           

    def to_representation(self, instance):
        return super(BookSerializer, self).to_representation(instance)

class BookCreateSerializer(serializers.Serializer):
    """Book create serializer"""
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=100)
    copies_available = serializers.IntegerField()

class BookEditSerializer(serializers.Serializer):
    """Book edit serializer"""

    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=100)
    copies_available = serializers.IntegerField()

class BorrowedBookSerializer(serializers.ModelSerializer):
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """Book Serializer"""
    class Meta:
        model = BorrowedBook
        fields = "__all__"

    def update(self, instance, validated_data):
        # import pdb; pdb.set_trace()
        student = LibararyUser.objects.get(id = validated_data.get("student"))
        books_query =  Book.objects.filter(id__in = validated_data.get("book"))
        instance.student  = student
        instance.borrow_date = validated_data.get("borrow_date")
        instance.issue_date = validated_data.get("borrow_date")
        instance.return_date = validated_data.get("borrow_date")
        instance.save()
        
        # issue_book = instance(
        #     student = student,
        #     borrow_date = validated_data.get("borrow_date"),
        #     issue_date = validated_data.get("borrow_date"),
        #     return_date = validated_data.get("return_date"),
        #     book = books_query
           
        # )
        # print(issue_book, type(issue_book), "++++++++++++++ issue book")
        instance.book.set(books_query)
        
        return True
    
        
        # import pdb; pdb.set_trace()
    
class BorrowedBookEditSerializer(serializers.ModelSerializer):
    """Book create serializer"""
    student = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    borrow_date = serializers.DateField()
    issue_date = serializers.DateTimeField()
    return_date = serializers.DateField()

    class Meta:
        model = BorrowedBook
        fields = "__all__"
