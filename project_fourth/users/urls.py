from django.urls import path
from .views import SignUpView,UserLogoutView
urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
