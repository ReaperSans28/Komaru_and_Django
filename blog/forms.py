from django import forms

from blog.models import Post
from config.forms import StyleFormMixin


class PostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name", "description", "image", "is_public"]
