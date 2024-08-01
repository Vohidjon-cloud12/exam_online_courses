from django.urls import path

from teachers import views

urlpatterns = [
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),

]