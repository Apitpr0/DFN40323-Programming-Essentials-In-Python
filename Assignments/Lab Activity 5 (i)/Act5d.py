import modSumAvg as sa

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2st number:"))
num3 = int(input("Enter 3st number:"))
hasil = sa.tambah(num1, num2, num3)
print("Sum is: " + str(hasil))
print("Average is: " + str(sa.purata(num1, num2, num3)))
