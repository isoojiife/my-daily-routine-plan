# ASCII Value Checker
print("=== ASCII Value Checker ===")

character = input("Enter one character: ")

if len(character) == 1:
    ascii_value = ord(character)
    print("The ASCII value of", character, "is", ascii_value)
else:
    print("Please enter only ONE character.")