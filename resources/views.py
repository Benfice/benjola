from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Resource


class ResourceListView(LoginRequiredMixin, ListView):
    model = Resource
    context_object_name = "resource_list"
    template_name = "resources/resource_list.html"
    login_url = "account_login"


class ResourceDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView,):
    model = Resource
    context_object_name = "resource"
    template_name = "resources/resource_detail.html"
    login_url = "account_login"
    permission_required = "resources.special_status"


class SearchResultsListView(ListView):
    model = Resource
    context_object_name = "resource_list"
    template_name = "resources/search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Resource.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    