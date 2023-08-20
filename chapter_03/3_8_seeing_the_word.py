#create a list of 5 locations and print
locations = ["hawaii", "italy", "alaska", "california", "arizona"]
print("Original Order:")
print(locations)

#print list in alphabetical order
print("\nAlphabetical:")
print(sorted(locations))

#show list is still in its orginal order
print("\nOriginal order:")
print(locations)

#use sorted to print list in reverse-alphabetical order
print("\nReverse alphabetical:")
print(sorted(locations,reverse=True))

#show list is still in its orginal order
print("\nOriginal order:")
print(locations)

#reverse the order of the list and print
print("\nReversed:")
locations.reverse()
print(locations)

#reverse the order of the list back to its original order and print
print("\nReversed again back to orginal:")
locations.reverse()
print(locations)

#use sort to change list to be in alphabetical order
print("\nAlphabetical:")
locations.sort()
print(locations)

#use sort to change list so it's stored in reverse-alphabetical order
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)