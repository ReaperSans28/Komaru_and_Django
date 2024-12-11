from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list)
    # path("home/", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
]
