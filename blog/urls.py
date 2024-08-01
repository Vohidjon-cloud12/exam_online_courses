from django.urls import path

from blog import views

urlpatterns = [
    path('blogs/', views.BlogPostListView.as_view(), name='blog_post_list'),  # For general list
    path('blogs/category/<int:pk>/', views.BlogPostListView.as_view(), name='category_filter'),
    path('single/<int:pk>/', views.SingleTemplateView.as_view(), name='blog-detail'),

]