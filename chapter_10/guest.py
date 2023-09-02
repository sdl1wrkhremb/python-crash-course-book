from pathlib import Path

name = input("Please enter your name: ")

path = Path('guest.txt')
path.write_text(name, encoding="utf-8")
