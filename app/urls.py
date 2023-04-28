from django.urls import path, include
from .views import LoginView, Home ,RegisterView,converastion,Send,LogOut,Reset

urlpatterns = [
    path('login',LoginView),
    path('logout',LogOut),
    path('ResetPassword',Reset),
    path('register',RegisterView),
    path('converastion/<int:id>/',converastion),
    path('send',Send),
    path('', Home),
]