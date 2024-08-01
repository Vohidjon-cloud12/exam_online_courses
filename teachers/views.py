from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from courses.models import Category
# Create your views here.
from teachers.models import Teacher


class TeacherListView(TemplateView):
    template_name = 'teachers/teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['teachers'] = Teacher.objects.all()
        return context


class TeacherDetailView(TemplateView):
    template_name = 'teachers/teachers-detail.html'

    def get_context_data(self, **kwargs):
        teacher = Teacher.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['teacher'] = teacher
        return context
