favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
coders = ["ryan", "jen", "edward", "bob",
          "fred", "phil", "john", "james", "sarah"]

for coder in coders:
    if coder in favorite_languages.keys():
        print(
            f"{coder.title()}\'s favorite coding language is {favorite_languages[coder].title()}")
    else:
        print(f"{coder.title()} please take the language poll!")
