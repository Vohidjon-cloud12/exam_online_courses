from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from django.db import models

from blog.models import Author, Blog
from courses.managers import CustomUserManager
from teachers.models import Teacher


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=299)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField()
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(upload_to='images/')

    @property
    def duration_of_video(self):
        if self.duration >= 60:
            hours = self.duration // 60
            minutes = self.duration % 60
            return hours, minutes

    def __str__(self):
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=299)
    video = models.FileField(upload_to='courses/')


class CourseComment(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    is_published = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    birth_of_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.password

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.name
