from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

print("\n--- Looping over the lines:")
for line in contents.splitlines():
    print(line)
