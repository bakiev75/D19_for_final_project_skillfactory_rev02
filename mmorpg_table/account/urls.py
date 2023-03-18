from django.urls import path
from .views import BaseRegisterView


urlpatterns = [
    # path('login/',
    #      LoginView.as_view(template_name = 'sign/login.html'),
    #      name='login'),
    # path('logout/',
    #      LogoutView.as_view(template_name = 'sign/logout.html'),
    #      name='logout'),
    path('',
         BaseRegisterView.as_view(template_name='registration.html'),
         name='create_user'),
]
