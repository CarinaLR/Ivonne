import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
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


# Block to add, update or delete Products by the admins

def adminProduct(request):
    allproducts = Product.objects.all()

    # Add new product via post request
    if request.method == "POST":
        prod_name = request.POST["newProdName"]
        prod_descpt = request.POST["newProdDescpt"]
        prod_price = request.POST["newProdPrice"]

        priceNum = float(prod_price)

        # Attempt to create new product

        product = Product.objects.create(
            name=prod_name, description=prod_descpt, price=priceNum)
        product.save()

        return render(request, "auctions/adminProduct.html")

    return render(request, "auctions/adminProduct.html", {
        "allProducts": allproducts
    })

# Block to Delete or Update product by id


def changingProduct(request, prod_id):
    allproducts = Product.objects.all()
    got_id = prod_id

    product_id = prod_id
    print("profuct to delete", product_id)

    return render(request, "auctions/adminProduct.html", {
        "allProducts": allproducts,
        "message": "Got product id to delete"
    })

# Block to return JSON response


def responseJSON(request):
    allproducts = Product.objects.all().order_by('pk')
    products_arr = []

    # Append each product to send response
    for product in allproducts:
        products_arr.append(
            {"id": product.id, "name": product.name, "description": product.description, "price": product.price})

    return JsonResponse(products_arr, safe=False)
