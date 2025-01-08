from django.urls import path
from .views import index, RegisterView, LoginView, TeaLeavesView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", index, name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("tealeaves/", TeaLeavesView.as_view(), name="tea-leaves"),
    
]