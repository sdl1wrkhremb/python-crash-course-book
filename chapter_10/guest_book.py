from pathlib import Path

path = Path('guest_book.txt')

prompt = ("Hi, what's your name? ")
prompt += ("(Enter 'quit' to exit.)")

guest_book = []

while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        guest_book.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_book:
    file_string += f"{name}\n"

path.write_text(file_string, encoding="utf-8")
