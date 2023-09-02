from pathlib import Path
import json

path = Path('favorite_number.txt')

try:
    saved_content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    number = input(("Hi, what's your favorite number? "))
    contents = json.dumps(number)
    path.write_text(contents, encoding="utf-8")
else:
    saved_number = json.loads(saved_content)
    print(saved_number)
