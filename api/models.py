from django.db import models
from django.conf import settings
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

class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    class OSTypes(models.TextChoices):
        MOBILE = "MOBILE", "Мобильная"
        DESKTOP = "DESKTOP", "Настольная"

    title = models.CharField(verbose_name="Название", max_length=60)
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    short_description = models.CharField(verbose_name="Короткое описание", max_length=100)
    image = models.ImageField(verbose_name="Картинка", blank=True)
    file = models.FileField(verbose_name="Файл", blank=True)
    downloads = models.PositiveBigIntegerField(verbose_name="Скачивания", default=0)
    price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    is_free = models.BooleanField(verbose_name="Бесплатно ли")
    os_type = models.CharField(verbose_name="Тип платформы", max_length=50, choices=OSTypes.choices)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField()

    @property
    def image_url(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продукта"


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
    rate = models.PositiveIntegerField(
        verbose_name="Оценка",
        validators=[validators.MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(verbose_name="Дата добавления", auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ("product", "user")


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

    class Meta:
        unique_together = ("product", "user")
