from django.core.exceptions import ValidationError
from django import forms

from catalog.models import Product
from catalog.utils import validate_disallowed_words
from config.forms import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category", "is_public"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if int(price) < 0:
            raise ValidationError("Цена не может иметь отрицательное значение")
        return price

    def clean_name(self):
        name = self.cleaned_data["name"]
        validate_disallowed_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        validate_disallowed_words(description)
        return description


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["is_public",]
