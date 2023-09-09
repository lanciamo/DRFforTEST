from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class BaseCommentSerializer(serializers.ModelSerializer):
    childs_count = serializers.SerializerMethodField()  # опять предлагает сделать статик

    class Meta:
        model = Comment
        fields = '__all__'

    def get_childs_count(self, obj):
        return obj.childs.count()


class RecursiveCommentSerializer(serializers.ModelSerializer):
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_childs(self, obj):  # почему она предлагает сделать метод статик?
        childs = obj.childs
        return RecursiveCommentSerializer(childs, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'

