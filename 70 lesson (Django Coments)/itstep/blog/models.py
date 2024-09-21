from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


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

    tags = models.ManyToManyField("Tag", related_name='blog_posts')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="posts")
    # image = models.ImageField(upload_to='post/images/')

    objects = models.Manager()
    published = PublisherManager()

    def __str__(self):
        return f"{self.title} - {self.pk}"

    class Meta:
        ordering = ["-publish"]
        verbose_name_plural = "Публікації"
        verbose_name = "Публікація"

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.pk])

    def save(self, *args, **kwargs):  # < here
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True, help_text='A label for name tag.')
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')

    def __str__(self):
        return f'Tag by {self.name}'

    class Meta:
        verbose_name = 'Tag'

    def save(self, *args, **kwargs):
        print("save to db")
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} - {self.email}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

        def __str__(self):
            return f'Comment {self.name} on {self.post}'
