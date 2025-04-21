from django.urls import path
from .views import userRegistrationview,UserLoginView,Logout,profile

urlpatterns = [
    path('register/', userRegistrationview.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('Logout/', Logout.as_view(),name='logout'),
    path('profile/', profile.as_view(),name='profile'),
]
