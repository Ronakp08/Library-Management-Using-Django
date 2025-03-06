from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BorrowedBookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowed-books', BorrowedBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrowed-books/borrowed_by/', BorrowedBookViewSet.as_view({'get': 'borrowed_by'}), name='borrowed_by'),
    path('borrowed-books/return_date/', BorrowedBookViewSet.as_view({'get': 'return_date'}), name='return_date'),
]