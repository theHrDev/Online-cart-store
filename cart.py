# Cart features:

# add to cart

# remove from cart

# view cart

# calculate total

# apply 5% discount if total > 200,000

products = {}

def add_to_cart(product, price):

    if product in products:
        return f"{product} already exists"
    
    products[product] = price
    return f"{product} added successfully"

def remove_cart(product):
    if product not in products:
        return f"{product} not on the cart"
    del products[product]
    return f"{product} removed from the cart"

def view_cart():
    print("Your cart are listed below: ")
    return products
    
def calculate_total():
    discounted_price = 0
    total_price = 0
    for price in products:
        discounted_price += int(price)
        if discounted_price > 200000:
            total_price = 0.05 * discounted_price
        else:
            total_price = discounted_price
            
    return total_price


def cart_store(menu):
    if menu == "1":
        product = input("Enter the product: ")
        price = input("Enter the price: ")
        print(add_to_cart(product,price))
    elif menu == "2":
        print(remove_cart())
    elif menu == "3":
        print(view_cart())
    elif menu == "4":
        print(calculate_total())
    else:
        print("Invalid menu")
        
    repeat = input("Do you want to perform another action? \n 1.yes 2.no: ")
    if repeat == "1":
        menu = input("Enter a menu to get started \n1.Add to cart \n2.Remove from cart \n3.View Cart \n4.Calculate Total: \n   ")
        cart_store(menu=menu)
    else:
        print("Thanks for shopping with us")
        
menu = input("Enter a menu to get started \n1.Add to cart \n2.Remove from cart \n3.View Cart \n4.Calculate Total: \n   ")
cart_store(menu=menu)