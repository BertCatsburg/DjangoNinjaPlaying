from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
# from ninja import NinjaAPI
#
# api = NinjaAPI(title="BERT Test Api", version="1.0.0")
#
#
# @api.get("/add")
# def add(request, a: int, b: int):
#     return {"result": a + b}
#
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/", api.urls),
# ]
