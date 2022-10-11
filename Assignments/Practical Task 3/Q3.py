order = {
    "customerName": "Mikael",
    "customeID": 1234,
    "customerOrder": "Spagetti"
}

#a. Add new item "customerPrice":RM13.90 to the dictionary
print("Add new item customerPrice:RM13.90 to the dictionary")
order["customerPrice"] = "RM13.90"
print(order)
print("\n")

#b. Change the value of customerID to 5678
print("Change the value of customerID to 5678")
order["customeID"] = 5678
print(order)
print("\n")

#c. Remove the last item in the dictionary
print("Remove the last item in the dictionary")
order.popitem()
print(order)
print("\n")

#d. clear all the items in the dictionary
print("clear all the items in the dictionary")
order.clear()
print(order)
print("\n")
