from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, profile_view, RegisterView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="products_create"),
    path(
        "catalog/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "catalog/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete"
    ),
    path('profile', profile_view, name="profile"),
    path('register', RegisterView.as_view(), name="register"),
]
