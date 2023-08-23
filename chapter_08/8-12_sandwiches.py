# function for ordering a sandwich
def order_sandwich(*toppings):
    """assemble the sandwich that was ordered with the requested toppings"""
    print("\nWe've received your order: ")
    for topping in toppings:
        print(f"adding {topping} to your sandwich")
    print("your sandwich is ready!")


order_sandwich('tomatoes')
order_sandwich('tomatoes', 'onions', 'spinach')
order_sandwich('tomatoes', 'onions', 'spinach', 'cucumbers', 'banana peppers')
