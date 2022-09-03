a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print("a =", a, ":", bin(a), "b =", b, ":", bin(b))
c = 0

c = a & b  # 12 = 0000 1100
print("Result of AND is",c,':',bin(c))

c = a|b    # 61 = 0011 1101
print("Result of OR is",c,':',bin(c))

c=a^b      # 49 = 0011 0001
print("Resukt of EXOR is",c,':',bin(c))

c=~a    # -61 = 1100 0011
print("Result of COMPLEMENT is",c,':',bin(c))

c=a<<2  # 240 = 1111 0000
print("Result of LEFT SHIFT is",c,':',bin(c))

c=a>>2  #15 = 0000 1111
print("Result of RIGHT SHIFT is",c,':',bin(c))