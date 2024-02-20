# from django.http import HttpResponse
# from .models import Author
# from .models import Author, Book
# from django.views import View
# from django.urls import reverse
# from django.shortcuts import render

# # def index(request):
#     # authors_link = f"<a href={reverse('store:author_list')}>Authors</a>"
#     # books_link = f"<a href={reverse('store:book_list')}>Books</a>"
  
    
#     # content = f"<ul>{authors_link} {books_link}</ul>"
#     # return HttpResponse(content)

# def index(request):
#     num_of_books = Book.objects.all().count()
#     return render(request, "store/index.html", {"num_of_books": num_of_books})
    

# # class AuthorListView(View):
    
# #     def get(self, request):
# #         # Retrieving the full list of authors as queryset
# #         authors = Author.objects.all()
        
# #         # Initialize the content variable
# #         content = ""
        
# #         # Loop over the authors queryset
# #         for author in authors:
# #             # Create a HTML list element that includes each authors names
# #             new_author = f"<li>{author}</li>"
# #             # append the HTML element to content
# #             content += new_author
            
# #         return HttpResponse(content)

# class AuthorListView(View):
    
#     def get(self, request):
#         # Retrieving the full list of authors as queryset
#         authors = Author.objects.all()
#         return render(request, "store/author_list.html", {"authors": authors})
    
# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         return render(request, "store/book_list.html", {"books": books})
    

# class BookListView(View):
    
#     def get(self, request):
#         books = Book.objects.all()
#         content = ""
        
#         for book in books:
#             new_book = f"<li>{book} - {book.author}</li>"
#             content += new_book
            
#         return HttpResponse(content)
    

# class GenreListView(View):
    
#     def get(self, request):
#         genres = Genre.objects.all()
#         content = ""
        
#         for genre in genres:
#             new_genre = f"<li>{genre}</li>"
#             content += new_genre
            
#         return HttpResponse(content)

# views.py
# store/views.py


from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book

def index(request):
    num_of_books = Book.objects.all().count()
    return render(request, "store/index.html", {"num_of_books": num_of_books})

class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, "store/author_list.html", {"authors": authors})

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'store/book_list.html', {'bookss': books})
