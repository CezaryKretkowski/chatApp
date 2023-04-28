from django.urls import path, include
from .views import LoginView, Home ,RegisterView,converastion,Send,LogOut

urlpatterns = [
    path('login',LoginView),
    path('logout',LogOut),
    path('register',RegisterView),
    path('converastion/<int:id>/',converastion),
    path('send',Send),
    path('', Home),
]