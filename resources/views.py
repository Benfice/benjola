from django.views.generic import ListView, DetailView
from .models import Resource


class ResourceListView(ListView):
    model = Resource
    context_object_name = "resource_list"
    template_name = "resources/resource_list.html"


class ResourceDetailView(DetailView):
    model = Resource
    context_object_name = "resource"
    template_name = "resources/resource_detail.html"