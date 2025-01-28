from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalogs/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("catalogs/create", ProductCreateView.as_view(), name="products_create"),
    path("catalogs/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("catalogs/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete"),
]
