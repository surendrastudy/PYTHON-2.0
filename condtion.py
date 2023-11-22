age = 1

if age >=18:
    print("You are adult")

elif age < 18 and age > 5:
    print("You are in school")

else:
    print("You are a child")


# make a calculator

first = int(input("Enter a first number"))
operator = input("Enter a operator ")
second = int(input("Enter a second number"))


if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
elif operator == "*":
    print(first*second)

else:
    print("wrong choice")
