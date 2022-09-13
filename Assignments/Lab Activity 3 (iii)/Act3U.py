#create a list
alphabet = ['a', 'e', 'i', 'o', 'i', 'i', 'u']

#Search for index 'e' in the list
ind = alphabet.index('e')
print("Index of e =", ind)

#Search for 'i' after index 3
ind = alphabet.index('i', 3)
print("Index of i =", ind)

#Search for 'i' between index 3 and 5
ind = alphabet.index('i', 3, 5)
print("Index of i =", ind)
