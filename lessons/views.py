from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lesson


class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"
    template_name = "lessons/lesson_list.html"


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson"
    template_name = "lessons/lesson_detail.html"


class LessonCreateView(CreateView):
    model = Lesson
    template_name = "lessons/lesson_new.html"
    fields = ["title", "author", "body"]


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = "lessons/lesson_edit.html"
    fields = ["title", "body"]


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = "lessons/lesson_delete.html"
    success_url = reverse_lazy("lesson_list")