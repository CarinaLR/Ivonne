# Juzmooth

An e-Commerce site where Juzmooth clients can place an order and Juzmooth admins can manage products, databases, and tracking deliveries.

Tech Stack: `Python`/`Django`/`JavaScript`/ `Bootstrap4`/ `JQuery`/ `PostgrSQL`/ `Heroku`.

## Setup

```
# views.py -the core of the project structure, connects the app with the database, and all the corresponding paths for each web page.
# urls.py -determines the paths for each view function. Connects the HTTPrequest waiting for a matching response from views.py. Here we define the routes and arguments that we would need in order to fetch a call to our db.
# models.py -gives a perspective of how each table of the database looks like and what data types are referring to.
# templates folder -contains all HTML files.
# static folder -contains `auctions` folder which contains the css file with the stylesheet, all images using in the application, javascript file and a `readme` folder which contains the images for the readme file.
# main.js -connects the client-side with the server-side, here all the APIs calls are made to fetch information from our database. The path using in our fetch request has to match with the path on our urls.py to connect with the view function and retrieve information. Implementing AJAX to prevent refresh/ reloading the webpage which makes our app run fast.

```

## Enviroment

- `$ . venv/bin/activate`
- `cd commerce`
- `python manage.py makemigrations auctions`
- `python manage.py migrate`
- `python manage.py runserver`

## Home page client-view.

![](/auctions/static/auctions/readme/homePage.png)

## Home page - Products section.

![](/auctions/static/auctions/readme/products.png)

## Home page - Ingredients section.

![](/auctions/static/auctions/readme/ingredients.png)

## Home page - Footer section.

![](/auctions/static/auctions/readme/footer.png)

## Product page - Allow customer to add product to cart for checkout list.

![](/auctions/static/auctions/readme/addToCart.png)

## Checkout page - Allow customer to review products list to place an order.

![](/auctions/static/auctions/readme/checkout_1.png)

## Checkout page - Additional information will be prompt to the user to fill out a form before finished to order.

![](/auctions/static/auctions/readme/checkout_2.png)

## Home page admin-view.

![](/auctions/static/auctions/readme/homePageAdmin.png)

## Products list page admin-view. Allows admin to review product list, delete, update and create new product.

![](/auctions/static/auctions/readme/productList.png)

## Products list page admin-view. Allows admin to review product list, delete, update and create new product.

![](/auctions/static/auctions/readme/new_updateProduct.png)

## Order list page admin-view. Allows admin to review order list, mark the order as pending or delete the order.

![](/auctions/static/auctions/readme/orderList.png)

## Mobile responsive design with toggle navbar and scrolling down the page, using the bootstrap grid system.
