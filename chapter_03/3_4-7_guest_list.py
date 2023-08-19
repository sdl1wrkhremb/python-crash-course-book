friends = ["Bob", "Fred", "John"]

print(friends[0]+", please come to dinner")
print(friends[1]+", please come to dinner")
print(friends[2]+", please come to dinner")

print(f"\n{friends[1]} can no longer make it to dinner.")

del friends[1]
friends.insert(1,"Joe")

print(f"\n{friends[0]}, please come to dinner")
print(friends[1]+", please come to dinner")
print(friends[2]+", please come to dinner")

print("\nI JUST FOUND A BIGGER TABLE!!")

friends.insert(0, "James")
friends.insert(int(len(friends)/2), "Camry")
friends.append("Oakley")

print(f"\n{friends[0]}, please come to dinner")
print(friends[1]+", please come to dinner")
print(friends[2]+", please come to dinner")
print(friends[3]+", please come to dinner")
print(friends[4]+", please come to dinner")
print(friends[5]+", please come to dinner")

print("\nJK, I can only invite 2 guests now!!")

uninvite = friends.pop()
print(f"Sorry {uninvite}, you can no longer come.")
uninvite = friends.pop()
print(f"Sorry {uninvite}, you can no longer come.")
uninvite = friends.pop()
print(f"Sorry {uninvite}, you can no longer come.")
uninvite = friends.pop()
print(f"Sorry {uninvite}, you can no longer come.")

print(f"\n{friends[0]}, please come to dinner")
print(friends[1]+", please come to dinner")

del friends[0]
del friends[0]

print(friends)
