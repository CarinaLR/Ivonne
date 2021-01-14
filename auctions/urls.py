from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("adminProduct", views.adminProduct, name="adminProduct"),
    path("deleteProduct/<int:prod_id>",
         views.deleteProduct, name="deleteProduct"),
    path("responseJSON", views.responseJSON, name="responseJSON"),
    path("editProduct/<int:prod_id>",
         views.editProduct, name="editProduct"),
    path("product/<int:prod_id>", views.product, name="product"),
    path("addToList/<int:prod_id>", views.addToList, name="addToList"),
    path("checkout", views.checkout, name="checkout"),
    path("orderList_forAdmin", views.orderList_forAdmin, name="orderList_forAdmin"),
]
