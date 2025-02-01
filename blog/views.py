from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_public=True)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:posts_list")


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_path'] = self.request.path
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:posts_list")

    def get_success_url(self):
        return reverse("blog:posts_delete", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:posts_list")
