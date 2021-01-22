
from rest_framework import viewsets
from rest_framework_jwt.settings import api_settings
from portfolio.models import Portfolio, Post, Contact
from portfolio.serializers import UserSerializer, PortfolioSerializer, PostSerializer, ContactSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
    }


class PortfolioView(viewsets.ModelViewSet):
    
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PostView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ContactView(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer