from django.urls import path, include
from .views import signin, signup


urlpatterns = [
    path(route="signin", view=signin, name="signin"),
    path(route="signup", view=signup, name="signup"),
]

