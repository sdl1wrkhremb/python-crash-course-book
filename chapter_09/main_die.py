from die import Die

# create a 6 sided die
six_sided_die = Die()

# roll the die 10 times
print(f"Rolling {six_sided_die.sides} sided die:")
for x in range(1, 10):
    six_sided_die.roll_die()

# create a 10 sided die
ten_sided_die = Die(10)

# roll the die 10 times
print(f"Rolling {ten_sided_die.sides} sided die:")
for x in range(1, 10):
    ten_sided_die.roll_die()

# create a 20 sided die
ten_sided_die = Die(20)

# roll the die 10 times
print(f"Rolling {ten_sided_die.sides} sided die:")
for x in range(1, 10):
    ten_sided_die.roll_die()
