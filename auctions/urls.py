from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("adminProduct", views.adminProduct, name="adminProduct"),
    path("product/<int:prod_id>", views.product, name="product"),
    path("checkout", views.checkout, name="checkout"),

]
