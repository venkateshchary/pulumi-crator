import os
from faker import Faker
from django.contrib.auth.hashers import make_password

# 1. Point to your project's settings (replace 'myproject' with your actual project folder name)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django

# 2. Initialize Django
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

fake = Faker()
FAKE_PASSWORD = "I@m1993@User"

def create_users(n=10):
    user_list = []
    for _ in range(n):
        first_name = fake.first_name()
        email = fake.email()
        username = fake.unique.user_name()
        u = User(
            username=username,
            email=email,
            first_name=first_name,
            password=make_password(FAKE_PASSWORD),
        )
        user_list.append(u)
    User.objects.bulk_create(user_list)


if __name__ == "__main__":
    create_users()