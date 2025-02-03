from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache().filter(is_public=True)


def products_by_category_view(request, category_id):
    products = get_products_by_category(category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'catalog/products_by_category.html', {'products': products, 'category': category})


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_path'] = self.request.path
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.update_product"):
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm(
                "catalog.delete_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
