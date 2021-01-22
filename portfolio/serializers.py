from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, StringRelatedField

from portfolio.models import Portfolio, Post, Contact

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'home_description')


class PostSerializer(ModelSerializer):
    category = StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'short_description', 'post_text', 'use_in_home_screen', 'category')


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'portfolio', 'contact_text')