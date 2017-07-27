def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multipying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

age = add(40, 6)
height = subtract(180, 6)
weight = multiply(37, 2)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"A puzzle: {what}")
