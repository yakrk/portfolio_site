from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from .models import *
from django.contrib import messages, auth
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.


def commerce_top(request):
    product_categories = ProductCategory.objects.all()
    context = {"product_categories": product_categories}
    return render(request, "commerce\commerce-top.html", context)


def category_top(request, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category_name=category_id).filter(
        product_is_published=True
    )
    context = {"category": category, "products": products}
    return render(request, "commerce/category-top.html", context)


def product_details(request, category_id, product_id):
    # collect product information to display
    product_info = get_object_or_404(Product, pk=product_id)
    product_price = ProductPrice.objects.get(product=product_info)
    stock = Stock.objects.get(product=product_id)
    cart_amount = request.POST.get("amount")

    if request.method == "POST":
        if request.user.is_authenticated:
            # add to cart
            cart, created = Cart.objects.get_or_create(user=request.user)
            try:
                product_already_in_cart = CartItem.objects.get(
                    cart_id=cart.id, product=product_info
                )
            except:
                product_already_in_cart = None
            # if same product is already in cart, sum amount
            if product_already_in_cart:
                cart_amount = int(cart_amount)
                cart_amount += product_already_in_cart.amount
            # add to cartitem table
            cartitem, created = CartItem.objects.update_or_create(
                product=product_info,
                cart_id=cart,
                defaults={
                    "amount": int(cart_amount),
                    "price_with_tax": product_price.price_with_tax,
                },
            )
            cart.save()
            messages.success(request, 'Successfully added to cart')

        else:
            # if user is not logged in but presses add to cart button
            messages.error(request, "Please register account to add to cart")
            return redirect("register")

    if product_info.product_is_published == True:
        # create options for amout selection pulldown
        select_values = []
        for i in range(stock.remaining_stock):
            select_values.append(i + 1)

        # set context
        context = {
            "product_info": product_info,
            "price": product_price,
            "stock": stock,
            "select_values": select_values,
        }
        return render(request, "commerce/product-details.html", context)
    else:
        raise Http404("Product does not exist")


def cart_top(request):
    if request.user.is_authenticated:
        # if user clicked checkout
        if request.method == "POST":
            purchase_status = False
            # check availability of stock and payment
            cart = Cart.objects.get(user=request.user)
            cartitems = CartItem.objects.filter(cart_id=cart.id)
            for item in cartitems:
                if is_stock_available(request.user, item.product):
                    # continue to payment
                        purchase_status = True
                else:
                    # if stock is not available, return to cart_top with error message.
                    messages.error(
                        request,
                        f"Stock not available for {item.product.product_name}. Please update your cart.",
                    )
                    return redirect("cart_top")
            # if stock and payment is valid
            if purchase_status:
                save_to_purchase_history(request.user, cart, cartitems)
                reduce_stock(item.product, item.amount)
                # return cart_end page
                return redirect('cart_end')
        else:
            # if request is GET
            cart = Cart.objects.get(user=request.user)
            cartitems = CartItem.objects.filter(cart_id=cart.id)
            context = {
                "cart": cart,
                "cartitems": cartitems,
            }
            return render(request, "commerce/cart-top.html", context)
    else:
        messages.error(request, "Please login to see your cart")
        return redirect("login")


def is_stock_available(user, product):
    ## get cart
    cart = Cart.objects.get(user=user)
    cartitem = CartItem.objects.get(cart_id=cart.id,product=product)
    ## get available stock
    remaining_stock = Stock.objects.get(product=cartitem.product)
    if int(remaining_stock.remaining_stock) >= cartitem.amount:
        # if stock is available,  continue to payment
        return True
    else:
        return False
    
def reduce_stock(product, amount):
    stock = Stock.objects.get(product=product)
    stock.remaining_stock -= amount
    stock.save()

def save_to_purchase_history(user, cart, cartitems):
    purchase_history = PurchaseHistory(
        user=user,
        purchased_date = datetime.now(),
        total_price = cart.total_price,
        )
    purchase_history.save()
    # if payment is successful save to history
    for item in cartitems:
        purchased_item = PurchaseItem(
                purchase_id = purchase_history,
                product=item.product,
                amount=item.amount,
                purchased_price = item.price_with_tax,
                subtotal = item.cart_item_price,
            )
        purchased_item.save()

def cart_item_delete(request, cart_item_id):
    if request.user.is_authenticated:
        cartitem = CartItem.objects.get(id=cart_item_id)
        cartitem.delete()
        cart = Cart.objects.get(user=request.user)
        cart.save()
        return redirect("cart_top")
    else:
        messages.error(request, "Please login to see your cart")
        return redirect("login")


def cart_end(request):
    return render (request, "commerce/cart-end.html")


def purchase_history(request):
    purchase_history = PurchaseHistory.objects.filter(user=request.user).order_by("-purchased_date")
    context = {
        "purchase_history": purchase_history
    }
    return render(request, "commerce/purchase-history.html", context)


def purchase_history_details(request, purchase_id):
    purchase_history = PurchaseHistory.objects.get(user=request.user, id=purchase_id)
    purchase_details = PurchaseItem.objects.filter(purchase_id = purchase_id)
    context = {
        "purchase_history":purchase_history,
        "purchase_details":purchase_details,
    }
    return render(request, "commerce/purchase-history-details.html", context)


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect("register")
                else:
                    # create user
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        is_staff=False,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request, "You are now registered and can login")
                    return redirect("login")

        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, "commerce/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        # user exists?
        if user is not None:
            auth.login(request, user)
            return redirect("commerce_top")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "commerce/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("login")
