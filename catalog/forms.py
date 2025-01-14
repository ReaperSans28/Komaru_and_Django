from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product

invalid_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


def validate_disallowed_words(value):
    if any(disallowed_word in value.lower() for disallowed_word in invalid_words):
        raise ValidationError("ОСУЖДАЮ.")


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data['price']
        if int(price) < 0:
            raise ValidationError("Цена не может иметь отрицательное значение")
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        validate_disallowed_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        validate_disallowed_words(description)
        return description
