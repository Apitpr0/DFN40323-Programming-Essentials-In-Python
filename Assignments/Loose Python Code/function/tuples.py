#first tuple (ordered and unchangeable and allow duplicate values)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

mekdi = ["Mekciken", "BigMek", "Dobolcis", "Mellow"]
mekdi.insert(0, "Mellow")
print(mekdi)
'''
#Change tuple values (convert to list --> change list --> convert back to tuple)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
'''
'''
x = ("apple", "banana", "cherry")
x[1] = "kiwi"
print(x)
'''

#Add tuple values (convert to list --> add things to list --> convert back to tuple)
thistuple2 = ("apple", "banana", "cherry")
y = list(thistuple2)
y.append("orange")
thistuple2 = tuple(y)
print(thistuple2)

#Delete tuple values (convert to list --> delete things in list --> convert back to tuple)
'''
thistuple3 = ("apple", "banana", "cherry")
y = list(thistuple3)
y.remove("apple")
thistuple3 = tuple(y)
print(y)
'''
thistuple4 = ("apple", "banana", "cherry")
x = list(thistuple4)
del x
x = tuple(y)
print(y)

#loop through a tuple
loopTuple = ("apple", "banana", "cherry")
for x in loopTuple:
    print(x)

#Loop through index number
indexTuple = ("apple", "banana", "cherry")
for i in range(len(indexTuple)):
    print(indexTuple[i])