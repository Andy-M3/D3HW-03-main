from django.urls import path
from .views import SignUp, Logout,

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('signup', SignUp.as_view(), name='signup'),

]