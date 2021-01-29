from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from portfolio.views import PortfolioView, PostView, ContactView, JSONWebTokenAuthentication


urlpatterns = [
    path('login/', JSONWebTokenAuthentication.as_view()),
    path('refresh_token/', refresh_jwt_token),
    path('portfolio/', PortfolioView.as_view({'get': 'list'})),
    path('post/', PostView.as_view({'get': 'list', 'post': 'create'})),
    path('contact/', ContactView.as_view({'get': 'list', 'post': 'create'})),
]