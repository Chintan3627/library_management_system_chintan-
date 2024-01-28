from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializer import *

class Can_Add_Book(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff | request.user.user_type=="librariyan":
            return True
        return False
    

class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class BookViewSet(viewsets.ViewSet):
    """BookViewSet for create, update, delete and list Books"""

    permission_classes = (IsAuthenticated,) 
  
    def get_serializer_class(self):
        if self.action == "add":
            return BookCreateSerializer
        if self.action == "all":
            return BookSerializer
        if self.action == "get":
            return BookSerializer
        if self.action == "delete":
            return BookSerializer
        return BookEditSerializer

    @action(detail=False, methods=["post"], name="add")
    def add(self, request):
        """This method will create Book by dict"""

        serializer = BookSerializer
        serializer_obj = serializer(data=request.data)

        if serializer_obj.is_valid():
            try:
                
                serializer_obj.save()
                return Response(
                    data= {"message": "Book Created Successfully"},
                )
            except Exception as e:
                print(str(e), "++++++++++++ error while creating book")
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer_obj.errors,
        )

    @action(detail=False, methods=["get"], name="all")
    def all(self, request):
        serializer = BookSerializer
        queryset =  Book.objects.all()
        paginator = Pagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer_obj = serializer(paginated_queryset, many=True)
        paginated_data = paginator.get_paginated_response(serializer_obj.data).data
        message = "Successfully listed all Books."
        return Response(data=paginated_data)

    @action(detail=True, methods=["get"], name="get")
    def get(self, request, pk=None):
        """This method will get Book by pk"""
        get_serializer = BookSerializer
        try:
            Book_obj = Book.objects.get(pk=pk)
            response = get_serializer(Book_obj)
            return Response(
                data=response.data
            )
        except Exception as e:
            print(str(e), "+++++++ error while getting book")
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": str(e)}
            )

    @action(detail=True, methods=["patch"], name="edit")
    def edit(self, request, pk=None):
        serializer = BookSerializer
        serializer_obj = serializer(data=request.data)
        if serializer_obj.is_valid():
            try:
                Book_obj =  Book.objects.get(pk=pk)
                book = BookSerializer(Book_obj)
                book.update(Book_obj,serializer_obj.data)
               
                return Response(
                    data= {"message":"You have Edited Book data successfully"}
                )
            except Exception as e:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=str(e),
                )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer_obj.errors,
        )

    @action(detail=True, methods=["delete"], name="delete")
    def delete(self, request, pk=None):
        """This method will delete Book by pk"""
        try:
            Book_obj = Book.objects.get(pk=pk)
            Book_obj.delete()
            
            return Response(
                data = { 'message':"You have deleted successfully"}
            )
        except  Exception  as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )



class BorrowBookViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    # print(permission_classes,"permission_classes ")
    def get_serializer_class(self):
        if self.action == "add":
            return BorrowedBookSerializer
        if self.action == "all":
            return BorrowedBookSerializer
        if self.action == "get":
            return BorrowedBookSerializer
        if self.action == "delete":
            return BorrowedBookSerializer
        return BorrowedBookSerializer

    @action(detail=False, methods=["post"], name="add")
    def add(self,request):
        serializer = BorrowedBookSerializer
        serializer_obj = serializer(data=request.data)
        if serializer_obj.is_valid():
            try:
                
                serializer_obj.save()
                return Response(
                    data= {"message": "Books issued successfully"},
                )
            except Exception as e:
                print(str(e), "++++++++++++ error while creating book")
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer_obj.errors,
        )
    
    @action(detail=False, methods=["get"], name="all")
    def all(self, request):
        serializer = BorrowedBookSerializer
        queryset =  BorrowedBook.objects.all()
        # values('student__username','book__title','issue_date','return_date')
        paginator = Pagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer_obj = serializer(paginated_queryset, many=True)
        message = "Successfully listed all Books."
        return Response(data=serializer_obj.data)

    @action(detail=True, methods=["get"], name="get")
    def get(self, request,pk = None):
        get_serializer = BorrowedBookSerializer
        try:
            print(pk,'pk--------------')
            Book_obj = BorrowedBook.objects.get(pk=pk)
            response = get_serializer(Book_obj)
            return Response(
                data=response.data
            )
        except Exception as e:
            print(str(e), "+++++++ error while getting book")
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": str(e)}
            )
        pass
    
    @action(detail=True, methods=["patch"], name="edit")
    def edit(self, request,pk =None):
        # import pdb; pdb.set_trace()

        serializer = BorrowedBookSerializer
        serializer_obj = serializer(data=request.data)
        if serializer_obj.is_valid():
            try:
                borrowedbookobj =  BorrowedBook.objects.get(id=pk)
                borrow_book = serializer(borrowedbookobj)
                borrow_book.update(instance=borrowedbookobj, validated_data= serializer_obj.data)
                # serializer_obj.save()
               
                """
                Book_obj =  Book.objects.get(pk=pk)
                book = BookSerializer(Book_obj)
                book.update(Book_obj,serializer_obj.data)
                """

                return Response(
                    data= {"message":"You have Edited broow book data successfully"}
                )
            except Exception as e:
                print(e,'-----+++++++++++-----------')
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=str(e),
                )
           
    @action(detail=False, methods=["delete"], name="delete")
    def delete(self, request,pk = None):
        try:
            Book_obj = BorrowedBook.objects.get(pk=pk)
            Book_obj.delete()
            
            return Response(
                data = { 'message':"You have deleted successfully"}
            )
        except  Exception  as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
    