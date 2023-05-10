from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.love, name = "love"),
    path('favicon.ico', RedirectView.as_view(url='/static/orders/favicon.ico')),
    path("home/", views.home, name = "home"),
    path("menu/", views.index, name="index"),
    path("add/", views.additems, name="additems"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("allorders/", views.allorders, name="allorders"),
    path("complete/", views.complete, name="complete"),
    path("delete/", views.delete, name="delete"),
    path("myorders/", views.myorders, name="myorders"),
]
