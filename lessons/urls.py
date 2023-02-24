from django.urls import path
from .views import (
    LessonListView, 
    LessonDetailView, 
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView,
)

urlpatterns = [
    path("", LessonListView.as_view(), name="lesson_list"),
    path("<uuid:pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("new/", LessonCreateView.as_view(), name="lesson_new"),
    path("<uuid:pk>/edit/", LessonUpdateView.as_view(), name="lesson_edit"),
    path("<uuid:pk>/delete/", LessonDeleteView.as_view(), name="lesson_delete"),
]
