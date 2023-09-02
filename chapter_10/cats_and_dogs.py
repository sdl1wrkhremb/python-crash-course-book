from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogs.txt')


def read_file(path):
    """read file from given path"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} was not found.")
        # pass (fail silently)
    else:
        print(f"The content from {path} reads: ")
        print(contents)


read_file(cats_path)
read_file(dogs_path)
