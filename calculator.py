a = int(input())
op = input()
b = int(input())
if op == "+":
    result = a + b
if op == "-":
    result = a - b
if op == "*":
    result = a * b
if op == "/":
    if b == 0:
        print("can't devide by zero")
    result = a / b
if op == "**":
    result = a ** b
if op == "sqrt":
    if b == 0:
        print("can't perform operation")
    result = a ** (1 / b)
print(result)