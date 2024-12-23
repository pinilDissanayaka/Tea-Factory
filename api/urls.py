from django.urls import path, include
from .views import all_records, single_record

urlpatterns = [
    path("", all_records, name="all_records"),
    path("record/<str:user>/", single_record, name="single_record")
]

