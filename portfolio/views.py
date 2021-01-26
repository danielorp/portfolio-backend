from datetime import datetime
from email.utils import format_datetime

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from portfolio.models import Contact, Portfolio, Post
from portfolio.serializers import (ContactSerializer, PortfolioSerializer,
                                   PostSerializer, UserSerializer)

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

class JSONWebTokenAuthentication(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = format_datetime((datetime.now() +
                              api_settings.JWT_EXPIRATION_DELTA))
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortfolioView(viewsets.ModelViewSet):
    
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PostView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ContactView(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
