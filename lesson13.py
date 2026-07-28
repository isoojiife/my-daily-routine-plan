#Activity1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print("Before swapping:")
print("Number 1 =", num1)
print("Number 2 =", num2)
print("Number 3 =", num3)

temp = num1
num1 = num2
num2 = num3
num3 = temp

print("After swapping:")
print("Number 1 =", num1)
print("Number 2 =", num2)
print("Number 3 =", num3)