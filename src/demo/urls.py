from django.urls import path
from .views import register_user_view, login_user_view, logout_user_view


app_name = 'demo'

urlpatterns = [
    path('signup/', register_user_view, name='register'),
    path('signin/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout')
]
