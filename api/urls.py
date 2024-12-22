from django.urls import path, include
from .views import all_records

urlpatterns = [
    path("", all_records, name="all_records")
]

