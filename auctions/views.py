import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Product, OrderProduct

# Set global variables
cartList = []
count = 0


def index(request):
    in_cart = len(cartList)
    return render(request, "auctions/index.html", {
        "in_cart": in_cart
    })


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
            prod_id = product.id
            prod_name = product.name
            prod_descpt = product.description
            prod_price = product.price

    return render(request, "auctions/product.html", {
        "prod_id": prod_id,
        "prod_name": prod_name,
        "prod_descpt": prod_descpt,
        "prod_price": prod_price
    })

# Block to display list of item in cart


def checkout(request):
    print("reach cartList", cartList)
    num_items = len(cartList)
    send_cartList = cartList
    if len(cartList) != 0:
        for item in cartList:
            item_name = item.name
            item_price = item.price
            print(f"items in cart: {item_name}, {item_price}",)
            return render(request, "auctions/checkout.html", {
                "item_name": item_name,
                "item_price": item_price,
                "items": num_items
            })
    return render(request, "auctions/checkout.html", {
        "inCart": send_cartList,
        "items": num_items
    })


# Block to add item to the checkout list


def addToList(request, prod_id):
    addProd_id = prod_id
    print("addProd_id", addProd_id)

    if request.method == "POST":
        get_prod = Product.objects.get(pk=addProd_id)
        cartList.append(get_prod)
        print("cartList", cartList)
        print("count", count)

        if len(cartList) != 0:
            for item in cartList:
                item_name = item.name
                item_price = item.price
                print(f"items in cart: {item_name}, {item_price}",)

    return HttpResponse(status=204)


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

        return render(request, "auctions/adminProduct.html", {
            "allProducts": allproducts
        })

    return render(request, "auctions/adminProduct.html", {
        "allProducts": allproducts
    })

# Block to Delete or Update product by id


def deleteProduct(request, prod_id):
    allproducts = Product.objects.all()
    got_id = prod_id

    product_id = prod_id
    print("profuct to delete", product_id)

    to_delete = Product.objects.get(pk=product_id)
    p_name = to_delete.name
    p_descpt = to_delete.description
    p_price = to_delete.price

    print("name: ", p_name, "price: ", p_price)
    print("description: ", p_descpt)

    # Attempt to delete product

    product = Product.objects.get(pk=product_id)
    product.delete()

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


@csrf_exempt
def editProduct(request, prod_id):
    print("reach func editProduct")
    # Get product by id
    get_prod = Product.objects.get(pk=prod_id)
    print("product_id, ", get_prod)

    if request.method == "PUT":
        print("get put request")
        data = json.loads(request.body)
        print("data", data)
        get_prod.name = data["name"]
        # get_prod.price = float(data["price"])
        # get_prod.description = data["description"]
        # print(f"changed: ", get_prod.id, get_prod.name,
        #       get_prod.price, get_prod.description)
        get_prod.save()

    return HttpResponse(status=204)
