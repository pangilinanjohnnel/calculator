operator= input ("enter operator (+ - * /): ")
while operator not in ("+", "-", "*", "/"):
    operator = input("please try again, invalid operator! enter operator (+ - * /):")

while True:
    try:
        num1 = float(input("Enter num1: "))
        break
    except ValueError:
        print("Invalid number. Please enter a valid numeric value.")


while True:
    try:
        num2 = float(input("Enter num2: "))
        break
    except ValueError:
        print("Invalid number. Please enter a valid numeric value.")


if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print("syntax error")

