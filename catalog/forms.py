from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from catalog.models import Product
from users.models import CustomUser

invalid_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


def validate_disallowed_words(value):
    if any(disallowed_word in value.lower() for disallowed_word in invalid_words):
        raise ValidationError("ОСУЖДАЮ.")


# def create_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.owner = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', "created_at", "updated_at", "was_publication", "owner"]

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


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("was_publication",)


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)
