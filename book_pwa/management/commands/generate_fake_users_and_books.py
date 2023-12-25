from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.utils.crypto import get_random_string
from faker import Faker

from book_pwa.models import Author, Book, Genre, Review

User = get_user_model()


class Command(BaseCommand):
    help = "Generating fake users and book"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "total_users", type=int, help="shows the nums of fake users"
        )
        parser.add_argument(
            "total_books", type=int, help="shows the nums of fake books"
        )

    def handle(self, *args, **kwargs):
        total_users = kwargs["total_users"]
        total_books = kwargs["total_books"]

        self.stdout.write(
            self.style.SUCCESS(f"Generating {total_users} fake users...")
        )
        self.generate_fake_users(total_users)

        self.stdout.write(
            self.style.SUCCESS(f"Generating {total_books} fake books...")
        )

        self.generate_fake_books(total_users)

        self.stdout.write(self.style.SUCCESS("Fake data generation complete."))

    def generate_fake_users(self, total_users):
        for i in range(total_users):
            fake = Faker()
            name = fake.name()
            username = fake.user_name() + str(i)
            email = fake.email()
            password = get_random_string(length=12)
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            Author.objects.create(name=name, user=user)

    def generate_fake_books(self, total_books):
        book_geners = [
            "Fantasy",
            "Adventure",
            "Romance",
            "Contemporary",
            "Dystopian",
            "Mystery",
            "Horror",
        ]
        for i in range(len(book_geners)):
            Genre.objects.create(name=book_geners[i])

        genres = Genre.objects.all()
        reviews_list = Review.objects.all()
        for i in range(total_books):
            fake = Faker()
            title = fake.user_name() + str(i)
            author = Author.objects.order_by("?").first()
            book = Book.objects.create(title=title, author=author)

            book.genre.set(
                genres.order_by("?")[: fake.random_int(min=1, max=3)]
            )
            book.reviews.set(
                reviews_list.order_by("?")[: fake.random_int(min=1, max=3)]
            )
