name_prompt = "Please enter your name: "
dream_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "Would you like to continue? yes/no "


responses = {}

while True:
    name = input(name_prompt)
    response = input(dream_prompt)

    responses[name] = response

    repeat = input(continue_prompt)
    if repeat == 'no':
        break


for name, dream in responses.items():
    print(f"{name.title()} would like to visit {dream.title()}.")
