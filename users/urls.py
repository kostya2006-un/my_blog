from django.urls import path
from users.views import user_login,user_logout,user_register,profile
app_name = 'users'

urlpatterns = [
    path('login/',user_login,name = 'user_login'),
    path('logout/',user_logout,name= 'user_logout'),
    path('registration/',user_register,name = 'user_register'),
    path('profile/',profile,name= 'profile')
]