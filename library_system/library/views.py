from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Book, BorrowedBook
from .serializers import UserSerializer, BookSerializer, BorrowedBookSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BorrowedBookViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

    # API to get books borrowed by a specific user
    @action(detail=False, methods=['get'])
    def borrowed_by(self, request):
        user_id = request.query_params.get('user_id')
        book_id = request.query_params.get('book_id')

        if user_id:
            borrowed_books = BorrowedBook.objects.filter(UserID=user_id)
        elif book_id:
            borrowed_books = BorrowedBook.objects.filter(BookID=book_id)
        else:
            return Response([])
        
        serializer = BorrowedBookSerializer(borrowed_books, many=True)
        return Response(serializer.data)

    # API to get the return date 
    @action(detail=False, methods=['get'])
    def return_date(self, request):
        user_id = request.query_params.get('user_id')

        borrowed_books = BorrowedBook.objects.filter(UserID=user_id)
        return_dates = borrowed_books.values('UserID', 'BookID__Title', 'ReturnDate')
        return Response(return_dates)