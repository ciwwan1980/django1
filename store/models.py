# store/models.py
from django.db import models
from django.utils.text import slugify

GENRE_CHOICES = (
    ('0', 'None'),
    ('1', 'Romance'),
    ('2', 'Sc-Fi'),
    ('3', 'Fantasy'),
    ('4', 'Drama'),
    ('5', 'Poetry'),
    ('6', 'Horror'),    
)

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default='0')
    date_of_birth = models.DateField(null=False)
    created_on = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    num_of_books = models.IntegerField()

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'],
                                    name="author_names_unique"),
        ]
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        get_latest_by = "created_on"
        indexes = [
            models.Index(fields=['last_name', 'first_name'], name="full_name_idx"),
            models.Index(fields=['genre'], name="genre_idx"),
        ]

    def __str__(self):
        return str(self.first_name +" " + self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    author = models.CharField(max_length=200, null=False)
    summary = models.TextField(max_length=1000, null=False)
    isbn = models.CharField(max_length=13, unique=True, help_text="13 character string - ISBN Number")
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default='0')
    date_of_publishing = models.DateField()
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    slug = models.SlugField()
    discount = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title + self.author))
        self.discount = self.price // 5 
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
