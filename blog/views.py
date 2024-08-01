from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic import ListView, TemplateView, View, FormView

from blog.forms import BlogCommentForm
from blog.models import Blog, Author
from courses.models import Course, Category


# Create your views here.
class BlogPostListView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.all()
        categories = Category.objects.all()

        # Handle category filtering
        category_id = self.kwargs.get('pk')
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            blogs = blogs.filter(
                category=category)  # Assuming your Blog model has a ManyToManyField named 'categories'
        authors = Author.objects.all()

        context['categories'] = categories
        context['blogs'] = blogs
        context['authors'] = authors
        return context


class SingleTemplateView(TemplateView):
    template_name = 'blog/single.html'

    def get_context_data(self, **kwargs):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        blog = Blog.objects.get(pk=self.kwargs['pk'])
        comments = blog.comments.all()
        authors = blog.auther_id.all()
        context = super().get_context_data(**kwargs)
        context['blog'] = blog
        context['authors'] = authors
        context['categories'] = categories
        context['blogs'] = blogs
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.is_published = True
            comment.blog_id = blog
            comment.save()
            return redirect(reverse('blog-detail', kwargs={'pk': blog.pk}))
        # If the form is not valid, re-render the context with the form errors
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
