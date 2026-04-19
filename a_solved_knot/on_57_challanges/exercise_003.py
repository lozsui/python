"""
Prompt for two numbers. Then print
NUMBER1 OPERATOR NUMBER2 = RESULT
Do operator shall be on of [+,-,*,/].
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
else:
    print(f"Unknown operator: {op}")
    exit(1)

print(f"{a} {op} {b} = {result}")