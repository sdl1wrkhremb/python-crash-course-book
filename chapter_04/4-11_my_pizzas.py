favorite_pizzas = ['pepperoni', 'hawaiian',
                   'veggie', 'mushroom', "ham", "cheese", "sasuage"]

friend_pizzas = favorite_pizzas[:]

print(friend_pizzas)

favorite_pizzas.append("olive")
friend_pizzas.append("cheeseless")

print("my favorite pizzas are ")
for pizza in favorite_pizzas:
    print(pizza)


print("\nmy friends favorite pizzas are ")
for pizza in friend_pizzas:
    print(pizza)
