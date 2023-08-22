sandwich_orders = ['veggie', 'pastrami', 'italian', 'pastrami',
                   'turkey', 'ham', 'pastrami', 'spicy', 'pickle', 'plain']
finished_sandwiches = []

print("Currently out of: Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"We finsished your {sandwich} sandwich!")
