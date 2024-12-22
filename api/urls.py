from django.urls import path, include
from .views import TeaLeavesCreate

urlpatterns = [
    path("", TeaLeavesCreate.as_view(), name="collected_tea_leaves")
]

