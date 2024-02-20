from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth',)
    list_display_links = ('first_name', 'last_name', 'email')
    ordering = ['first_name', 'last_name']
    fieldsets = [
        ('Names', {
            'fields': (('first_name', 'last_name',), )
        }),
        ('Contact', {
            'fields': ('email',)
        }),
        ('Miscellaneous', {
            'fields': ('date_of_birth', 'num_of_books')
        })
    ]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_publishing', 'price',)
    list_filter = ('author', 'date_of_publishing', 'in_stock')
    fields = [
        'title', 'author', 'summary', 'isbn',
        'genre', 'date_of_publishing',
        ('price', 'in_stock'),  # Fix the syntax error here
    ]
