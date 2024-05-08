from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post
from blogging.serializers import PostSerializer
from rest_framework import viewsets


class PostListView(ListView):
    context_object_name = "posts"
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    context_object_name = "posts"
    queryset = Post.objects.exclude(published_date__isnull=True)
    template_name = "blogging/detail.html"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_date")
    serializer_class = PostSerializer
