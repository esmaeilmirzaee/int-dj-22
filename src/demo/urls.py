from django.urls import path
from .views import (
    register_user_view,
    login_user_view,
    logout_user_view,
    home_view,
    premium_view,
    PremiumView
)


app_name = 'demo'

urlpatterns = [
    path('signup/', register_user_view, name='register'),
    path('signin/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout'),
    path('', home_view, name='home'),
    path('premium/', PremiumView.as_view(), name='premium'),
    # path('premium/', premium_view, name='premium')
]
