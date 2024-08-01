from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    education = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    auther_id = models.ManyToManyField(Author, blank=True)
    category = models.ForeignKey('courses.Category', blank=True, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(upload_to='images/')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)


class BlogComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name


