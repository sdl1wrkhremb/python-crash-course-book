usernames = ["ghost", "pirate123", "stormhacker",
             "mrrobot", "soccerfan1", "admin"]

for name in usernames:
    if name == "admin":
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

usernames = []

if usernames:
    for name in usernames:
        if name == "admin":
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("we need to find some users")
