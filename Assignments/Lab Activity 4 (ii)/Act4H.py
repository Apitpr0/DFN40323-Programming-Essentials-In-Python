#global scope
X = 400  #X and func assigned in module: global

def func(Y):  #Y and Z assigned in function: locals
    # local scope
    Z = X + Y
    return Z

func(1)  #func in module: result=401
print("The answer is", func(1))
