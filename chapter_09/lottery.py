from random import choice


def draw_winning_ticket(possibilities):
    winning_ticket = []
    for x in range(1, 5):
        # winning_ticket.append(lottery_pool[randint(0, len(lottery_pool)-1)])
        winning_ticket.append(choice(possibilities))
    return winning_ticket


def geneate_random_ticket(possibilities):
    ticket = []
    for x in range(1, 5):
        # winning_ticket.append(lottery_pool[randint(0, len(lottery_pool)-1)])
        ticket.append(choice(possibilities))
    return ticket


def check_ticket(my_ticket, winning_ticket):
    if my_ticket == winning_ticket:
        return True
    else:
        return False


lottery_pool = ['A', 'J', 'E', 'X', 'S', '1',
                '2', '3', '4', '5', '6', '7',
                '8', '9', '10']
my_ticket = geneate_random_ticket(lottery_pool)

# loop until my ticket wins
drawings = 0
while True:
    winning_ticket = draw_winning_ticket(lottery_pool)
    won = check_ticket(my_ticket, winning_ticket)
    drawings += 1
    if won:
        print(f"you finally won after {drawings} drawings!")
        print(f"your ticket: {my_ticket}")
        print(f"winning ticket: {winning_ticket}")
        break
