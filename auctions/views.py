from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Product, OrderProduct


def index(request):

    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# Block to get the clicked product to show product description


def product(request, prod_id):
    allproducts = Product.objects.all()

    if request.method == "POST":

        hideen_pro = request.POST.get("product_value")
        prod_id = int(hideen_pro)

    clicked_prod = prod_id

    for product in allproducts:
        if clicked_prod == product.id:
            prod_name = product.name
            prod_descpt = product.description
            prod_price = product.price

    return render(request, "auctions/product.html", {
        "prod_name": prod_name,
        "prod_descpt": prod_descpt,
        "prod_price": prod_price
    })


def checkout(request):
    return render(request, "auctions/checkout.html")


# Block to add, update or delete Products by admins


def adminProduct(request):
    if request.method == "POST":

        hideen_in = request.POST.get("hi")

        print("hideen_in", hideen_in)

    return render(request, "auctions/adminProduct.html")
