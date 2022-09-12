days = int(input("Number of days to rent the car: "))
membershiptype = int(input("Select the membership (1.Silver, 2.Gold, 3.Non-Member) : "))
print("      RECEIPT OF CAR RENTAL SHOP        ")
print("----------------------------------------")

if membershiptype == 1:
    price = 50 * 0.05
    rentprice = price * days
    print("Rental Price : RM ", rentprice)
elif membershiptype == 2:
    price = 50 * 0.10
    rentprice = price * days
    print("Rental Price : RM ", rentprice)
elif membershiptype == 3:
    price = 50
    rentprice = price * days
    print("Rental Price : RM ", rentprice)
else:
    print("The membership you entered not found. Please try again.")

if days >= 3:
    discount = rentprice * 0.10
    print("Discount : RM ", discount)
    final = rentprice - discount
    print("Final Price of Car Rental : RM ", final)

else:
    print("Error!")
