from django.urls import path
from .views import ResourceListView, ResourceDetailView, SearchResultsListView

urlpatterns = [
    path("", ResourceListView.as_view(), name="resource_list"),
    path("<uuid:pk>/", ResourceDetailView.as_view(), name="resource_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
