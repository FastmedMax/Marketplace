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


class Product(models.Model):
    title = models.CharField(verbose_name="Название", max_length=60)
    description = models.TextField(verbose_name="Описание")
    short_description = models.CharField(verbose_name="Короткое описание", max_length=100)
    image = models.ImageField(verbose_name="Картинка", blank=True)
    file = models.FileField(verbose_name="Файл", blank=True)
    downloads = models.PositiveBigIntegerField(verbose_name="Скачивания", default=0)
    price = models.FloatField(verbose_name="Цена", blank=True)
    is_free = models.BooleanField(verbose_name="Бесплатно ли")


class ProductRate(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        on_delete=models.CASCADE,
        related_name="rates"
        )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    rate = models.PositiveIntegerField(verbose_name="Оценка", validators=[validators.MaxValueValidator(10)])


class UserProduct(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
