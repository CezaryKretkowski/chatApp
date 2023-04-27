from django.urls import path, include
from .views import LoginView , Home ,RegisterView,converastion,Send

urlpatterns = [
    path('login',LoginView),
    path('register',RegisterView),
    path('converastion/<int:id>/',converastion),
    path('send',Send),
    path('', Home),
]