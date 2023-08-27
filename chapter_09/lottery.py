from random import randint
from random import random

my_ticket = ['A', 'E', '8', 'X']
lottery_pool = ['A', 'J', 'E', 'X', 'S', '1',
                '2', '3', '4', '5', '6', '7', '8', '9', '10']
winning_ticket = []
# add 10 numbers and five letters to the pool
# for x in range(1, 10):
#     number = randint(1, 100)
#     lottery_pool.append(number)


def draw_winning_ticket():
    ticket = []
    for x in range(1, 5):
        ticket.append(lottery_pool[randint(0, len(lottery_pool)-1)])
    return ticket


# print(len(lottery_pool))
# winning_ticket = draw_winning_ticket()
# print(winning_ticket)

# loop until my ticket wins
drawings = 0
while True:
    winning_ticket = draw_winning_ticket()
    drawings += 1
    if my_ticket == winning_ticket:
        print(f"you finally won after {drawings} drawings!")
        break
