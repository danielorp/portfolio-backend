from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from portfolio.views import PortfolioView, PostView, ContactView


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('portfolio/', PortfolioView.as_view({'get': 'list'})),
    path('post/', PostView.as_view({'get': 'list', 'post': 'create'})),
    path('contact/', ContactView.as_view({'get': 'list', 'post': 'create'}))
]