from django.urls import path
from .views import index, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", index, name="index"),
    path("register/", RegisterView.as_view(), name="register")

]