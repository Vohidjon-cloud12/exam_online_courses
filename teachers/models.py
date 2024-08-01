from django.db import models

from django.db import models


class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'Junior'
        MIDDLE = 'Middle'
        STRONG_MIDDLE = 'Strong-middle'
        SENIOR = 'Senior'

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    specialization = models.ForeignKey('courses.Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(choices=LevelChoices, default=LevelChoices.MIDDLE.value)

    def __str__(self):
        return self.full_name
