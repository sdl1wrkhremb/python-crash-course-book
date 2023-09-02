from pathlib import Path
import json


def get_stored_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_info(path):
    """Prompt for a new user's info'."""
    username = input("What is your name? ")
    game = input("What is your favorite game? ")
    animal = input("What is your favorite animal? ")
    user_dictionary = {
        'username': username,
        'game': game,
        'animal': animal,
    }
    contents = json.dumps(user_dictionary)
    path.write_text(contents)
    return user_dictionary


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_dictionary = get_stored_info(path)
    if user_dictionary:
        print(f"Welcome back, {user_dictionary['username']}!")
        print(f"I see your favorite game is {user_dictionary['game']}!")
        print(f"And, your favorite animal is a {user_dictionary['animal']}!")
    else:
        user_dictionary = get_new_info(path)
        print(
            f"We'll remember you when you come back, {user_dictionary['username']}!")


greet_user()
