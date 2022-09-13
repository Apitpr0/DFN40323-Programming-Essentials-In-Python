cars = ["Toyota", "BMW", "Volvo", "Honda", "Proton"]
print("Original List=", cars)

#sort ascending
cars.sort()
print("Sort Ascending=", cars)

#sort descending
cars.sort(reverse=True)
print("Sort Descending =", cars)

#sort by item length
cars.sort(key=len)
print("Sort By Length=", cars)
