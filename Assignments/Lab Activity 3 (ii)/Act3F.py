#Program for converting Temperature

temp = input(
    "Input the temperature you like to convert?(e.g., 55F, 200C etc.):")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    after_conv="Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    after_conv="Celsius"
else:
    print("Input proper convention")
    quit()

print("The temperature in", after_conv, "is", result, "degrees.")
