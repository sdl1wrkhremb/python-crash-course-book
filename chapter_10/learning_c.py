from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()

contents = contents.replace('Python', 'C')

print(contents)
