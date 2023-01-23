from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView

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