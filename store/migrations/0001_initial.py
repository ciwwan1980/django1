# Generated by Django 4.2.10 on 2024-02-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
                ("author", models.CharField(max_length=200)),
                ("summary", models.TextField(max_length=1000)),
                (
                    "isbn",
                    models.CharField(
                        help_text="13 character string - ISBN Number",
                        max_length=13,
                        unique=True,
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("0", "None"),
                            ("1", "Romance"),
                            ("2", "Sc-Fi"),
                            ("3", "Fantasy"),
                            ("4", "Drama"),
                            ("5", "Poetry"),
                            ("6", "Horror"),
                        ],
                        default="0",
                        max_length=30,
                    ),
                ),
                ("date_of_publishing", models.DateField()),
                ("in_stock", models.BooleanField(default=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("slug", models.SlugField()),
                ("discount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100, null=True)),
                ("last_name", models.CharField(max_length=100, null=True)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=100, unique=True),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("0", "None"),
                            ("1", "Romance"),
                            ("2", "Sc-Fi"),
                            ("3", "Fantasy"),
                            ("4", "Drama"),
                            ("5", "Poetry"),
                            ("6", "Horror"),
                        ],
                        default="0",
                        max_length=30,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("created_on", models.DateField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("num_of_books", models.IntegerField()),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
                "db_table": "author",
                "ordering": ["last_name", "first_name"],
                "get_latest_by": "created_on",
                "indexes": [
                    models.Index(
                        fields=["last_name", "first_name"], name="full_name_idx"
                    ),
                    models.Index(fields=["genre"], name="genre_idx"),
                ],
            },
        ),
        migrations.AddConstraint(
            model_name="author",
            constraint=models.UniqueConstraint(
                fields=("first_name", "last_name"), name="author_names_unique"
            ),
        ),
    ]