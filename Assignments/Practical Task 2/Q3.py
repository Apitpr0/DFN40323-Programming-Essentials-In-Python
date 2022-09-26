# a. Add a new element "Pesona" after "Jazz" in car
car = ["Ativa", "Harrier", "HR-V", "Jazz", "X70"]
print("Original List = ", car)
car.insert(4, "Pesona")
print("Add Pesona after Jazz = ", car)
print("\n")

# b. Change “Hyundai” to “Proton” in brand.
brand = ["Perodua", "Volkswagen", "Honda", "Hyundai", "BMW", "Lexus", "Toyota"]
print("Original List=", brand)
brand[3] = "Proton"
print("After changing Hyundai to Proton = ", brand)
print("\n")

# c. Remove “Honda” in brand.
print("Original List = ", brand)
brand.remove("Honda")
print("After removing Honda = ", brand)
print("\n")

# d. Sort brand in descending order.
print("Original List = ", brand)
brand.sort(reverse=True)
print("Descending List = ", brand)
print("\n")

# e. Combine car and brand
car.extend(brand)
print("Join List", car)
print("\n")
