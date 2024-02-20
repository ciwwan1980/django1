# store/urls.py
from django.urls import path
from .views import index, AuthorListView, BookListView

app_name = "store"

urlpatterns = [
    path("", index, name="home"),
    path("author/", AuthorListView.as_view(), name="author_list"),
    path('books/', BookListView.as_view(), name='book_list'),
]