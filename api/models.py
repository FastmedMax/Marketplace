from django.db import models

from django.core import validators
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(
        verbose_name="Почта",
        unique=True,
        validators=[validators.validate_email],
        error_messages={
            "unique": "Пользователь с таким email уже существует.",
        },)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    objects = UserManager()

