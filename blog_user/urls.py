from django.urls import path
from .views import Signup, HandleSignup, Login, logout

urlpatterns = [
    path('signup/', HandleSignup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout')
]
