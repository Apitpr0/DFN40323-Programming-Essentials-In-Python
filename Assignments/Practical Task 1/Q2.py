totalunit = int(input("Please enter number of units you consumed:"))
#if else statement to calculate totalprice
if (totalunit <= 200):
    totalprice = totalunit * 0.218
elif (totalunit > 200) & (totalunit <= 300):
    tariff1 = 200 * 0.218
    unit1 = totalunit - 200
    tariff2 = unit1 * 0.334
    totalprice = tariff1 + tariff2
elif (totalunit > 300) & (totalunit <= 600):
    tariff1 = 200 * 0.218
    unit1 = totalunit - 200
    tariff2 = 100 * 0.334
    unit2 = unit1 - 100
    tariff3 = unit2 * 0.516
    totalprice = tariff1 + tariff2 + tariff3
elif (totalunit > 600) & (totalunit <= 900):
    tariff1 = 200 * 0.218
    unit1 = totalunit - 200
    tariff2 = 100 * 0.334
    unit2 = unit1 - 100
    tariff3 = 300 * 0.516
    unit3 = unit2 - 300
    tariff4 = unit3 * 0.546
    totalprice = tariff1 + tariff2 + tariff3 + tariff4
else:
    print("The allocated block is not suitable for your usage")

print("Total Consumption (kWh)=", totalunit)
print("Amount to pay = RM", float(totalprice))

