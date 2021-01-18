import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Product, OrderProduct, Order

# Set global variables
cartList = []
cartCount = len(cartList)
count = 0
inCart_Total = []
final_list = []


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
    in_cart = len(cartList)

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
        "prod_price": prod_price,
        "in_cart": in_cart
    })

# Block to display list of item in cart


def checkout(request):
    print("reach cartList", cartList)
    send_cartList = cartList
    in_cart = len(cartList)

    to_display = []
    allItems_inCart = []
    itemsQty = 0
    finalPrices = []
    totalPay = 0

    if len(final_list) != 0:
        for item in final_list:
            final_cost = (int(item['qty']) * item['product'].price)
            # Call str.format(number) with "{:.2f}" as str and a float as number to return a string representation of the number with two decimal places.
            a_float = final_cost
            formatted_float1 = "{:.2f}".format(a_float)
            to_display.append(
                {'qty': item['qty'], 'product': item['product'], 'final_cost': formatted_float1})
            print('to_Display', to_display)

    # Block to show user the checkout list

    if len(to_display) != 0:
        for item in to_display:
            allItems_inCart.append({"qty": item['qty'], "product": item['product'].name,
                                    "price": item['product'].price, "final": item['final_cost']})
            itemsQty = len(allItems_inCart)
            finalPrices.append(float(item['final_cost']))
            totalPay = sum(finalPrices)
            # Call str.format(number) with "{:.2f}" as str and a float as number to return a string representation of the number with two decimal places.
            b_float = totalPay
            formatted_float2 = "{:.2f}".format(b_float)
            print("TotalSum", formatted_float2)
    # Block to make a post request and save order

    if len(allItems_inCart) != 0:
        print("allItems_InCart toDisplay ->", to_display)

        if request.method == "POST":
            user = request.user

            # Attemp to create new product ordered
            username = user
            prods_ordered = []

            for order in to_display:
                prods_ordered.append({"user": username, "ordered": True,
                                      "product": order['product'], "quantity": int(order['qty'])})

            print(f"username:{user} and userID: {user.id}")
            print("prod_ordered:", prods_ordered)

            for orderProd in prods_ordered:
                orderProduct = OrderProduct.objects.create(
                    user=orderProd['user'], ordered=orderProd['ordered'], product=orderProd['product'], quantity=orderProd['quantity']
                )
                orderProduct.save()

            # Take input information to attemp to create order for user

            order_by_user = []
            orderProds = OrderProduct.objects.all()
            order_by_user.append(orderProds[len(orderProds) - 1])

            name = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']
            address = request.POST['address']

            print(
                f"name: {name}, lastName: {lastName}, email: {email}, phoneNumber: {phoneNumber}, address: {address}, products: {order_by_user}")

            order = Order.objects.create(user=username, lastName=lastName, address=address,
                                         phoneNumber=phoneNumber, ordered=True)
            order.products.set(order_by_user)
            order.save()

        return render(request, "auctions/checkout.html", {
            "prod_list": to_display,
            "allItems_InCart": allItems_inCart,
            "itemsQty": itemsQty,
            "totalPay": formatted_float2,
        })


# Block to add item to the checkout list


def addToList(request, prod_id):
    addProd_id = prod_id
    print("addProd_id", addProd_id)
    show_qty = []

    if request.method == "POST":
        get_prod = Product.objects.get(pk=addProd_id)
        cartList.append(get_prod)
        proQty = request.POST.get("qty")
        show_qty.append({"qty": proQty, "product": get_prod})

        if len(cartList) != 0:
            for item in cartList:
                item_name = item.name
                item_price = item.price
                print(f"items in cart: {item_name}, {item_price}",)
                inCart_Total.append(item_price)

        if len(show_qty) != 0:
            for prodObj in show_qty:
                final_list.append(prodObj)
                print("final-list: ", final_list)

    return HttpResponse(status=204)


# Block to add, update or delete Products by the admins

def adminProduct(request):
    allproducts = Product.objects.all()
    in_cart = len(cartList)

    # Add new product via post request
    # Attemp to add product using access-token in git repo
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
            "allProducts": allproducts,
            "in_cart": in_cart
        })

    return render(request, "auctions/adminProduct.html", {
        "allProducts": allproducts,
        "in_cart": in_cart
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
        get_prod.price = float(data["price"])
        get_prod.description = data["description"]
        # print(f"changed: ", get_prod.id, get_prod.name,
        #       get_prod.price, get_prod.description)
        get_prod.save()

    return HttpResponse(status=204)

# Block to add list of product to order and update order list.


def orderList_forAdmin(request):

    print("reach ordeList --")

    return render(request, "auctions/orderListAdmin.html")
