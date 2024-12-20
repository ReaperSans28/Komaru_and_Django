from django.urls import path
from komaru_blog.apps import KomaruBlogConfig
from komaru_blog.views import (
    PostListView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
)

app_name = KomaruBlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path("komaru/", PostListView.as_view(), name="posts_list"),
    path(
        "komaru/<int:pk>/",
        PostDetailView.as_view(),
        name="posts_detail",
    ),
    path(
        "komaru/create", PostCreateView.as_view(), name="posts_create"
    ),
    path(
        "komaru/<int:pk>/update",
        PostUpdateView.as_view(),
        name="posts_update",
    ),
    path(
        "komaru/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="posts_delete",
    ),
]
