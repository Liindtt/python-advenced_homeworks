from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class PublisherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = ('DF', 'Draft')
        PUBLISHED = ('PB', 'Published')

    title = models.CharField(verbose_name="Назва поста", max_length=20)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="posts")

    objects = models.Manager()
    published = PublisherManager()

    def __str__(self):
        return f"{self.title} - {self.pk}"

    class Meta:
        ordering = ["-publish"]
        verbose_name_plural = "Публікації"
        verbose_name = "Публікація"


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title} - {self.user.username} - {self.rating}"

    class Meta:
        unique_together = ('post', 'user')
