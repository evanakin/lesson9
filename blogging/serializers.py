from django.contrib.auth.models import User
from rest_framework import serializers
from blogging.models import Post, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name="post-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "posts"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "text",
            "author",
            "created_date",
            "modified_date",
            "published_date",
            "categories",
        ]
