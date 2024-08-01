from django.urls import path

from courses.views.course import views
from courses.views.authentication import views as auth_views

urlpatterns = [
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_courses'),
    path('send-email/', auth_views.ContactView.as_view(), name='save_message'),
    path('login/', auth_views.login_page, name='login'),
    path('logout/', auth_views.logout_page, name='logout'),
    path('register/', auth_views.register_page, name='register'),
    path('activate/<uidb64>/<token>/', auth_views.activate, name='activate')]
