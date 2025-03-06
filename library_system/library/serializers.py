from rest_framework import serializers
from .models import Book, BorrowedBook, User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(source='BookID', read_only=True)
    user = UserSerializer(source='UserID', read_only=True)
    BookID = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    UserID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = BorrowedBook
        fields = ['BorrowedID', 'BookID', 'UserID', 'book', 'user', 'BorrowDate', 'ReturnDate']

    def create(self, validated_data):
        return BorrowedBook.objects.create(**validated_data)
