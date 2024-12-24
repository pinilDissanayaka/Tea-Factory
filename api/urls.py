from django.urls import path, include
from .views import ProductAPIViewInfo

urlpatterns = [
    path(route='product/info', view=ProductAPIViewInfo.as_view(), name="product info")
]

