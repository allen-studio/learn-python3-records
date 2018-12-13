def add(a, b): # 定义加法
    print(f"ADDING {a} + {b}")
    return a + b

def subtrack(a, b): # 定义减法
    print(f"SUBTRACK {a} - {b}")
    return a - b

def multiply(a, b):  # 定义乘法
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b): # 定义除法
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just function!")

age = add(30, 5)
height = subtrack(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age:{age}, Height:{height}, Weight:{weight}, IQ:{iq}")


# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtrack(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")
