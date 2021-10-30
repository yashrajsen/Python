'''
I leave my house
if it is cloudy
    I bring umbrella
otherwise
    I bring sun glasses
'''
#
# IF ELIF ELSE Statements
#

# IF with boolean values
#

# is_male = False
# is_tall = False

# if is_male and is_tall:
#     print("You are a tall Male ")
# elif is_male and not(is_tall):
#     print("You are a short Male")
# elif not(is_male) and is_tall:
#     print("Your are not a male but tall")
# else:
#     print("You are not male and not tall")

#
# IF statements with comparisions

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(22,23.432,23.235))

#
# Build a basic calculator
#
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
