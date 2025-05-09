import datetime

# Predefined items and prices (can be customized or extended)
items_catalog = {
    "milk": 30,
    "bread": 25,
    "eggs": 6,
    "rice": 60,
    "sugar": 40,
    "tea": 120,
    "coffee": 150
}

cart = {}

def display_items():
    print("\nAvailable Items:")
    print("{:<10} {:>10}".format("Item", "Price (Rs)"))
    for item, price in items_catalog.items():
        print("{:<10} {:>10}".format(item, price))
    print()

def add_to_cart():
    while True:
        item = input("Enter item name to add (or type 'done' to finish): ").lower()
        if item == 'done':
            break
        if item in items_catalog:
            qty = int(input(f"Enter quantity of '{item}': "))
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
        else:
            print("Item not found. Please choose from the available items.")

def generate_bill():
    print("\n" + "="*40)
    print("        SUPER MARKET BILL")
    print("="*40)
    print("Date & Time:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("-"*40)
    print("{:<10} {:>8} {:>10}".format("Item", "Qty", "Total(Rs)"))
    print("-"*40)
    
    total = 0
    for item, qty in cart.items():
        price = items_catalog[item]
        item_total = price * qty
        total += item_total
        print("{:<10} {:>8} {:>10}".format(item, qty, item_total))
    
    gst = total * 0.05
    grand_total = total + gst
    
    print("-"*40)
    print("{:<20} {:>15.2f}".format("Subtotal", total))
    print("{:<20} {:>15.2f}".format("GST (5%)", gst))
    print("{:<20} {:>15.2f}".format("Grand Total", grand_total))
    print("="*40)
    print("Thank you for shopping with us!")
    print("="*40)

# Run the billing system
display_items()
add_to_cart()
generate_bill()