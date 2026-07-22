#daily activity planner
print("Daily Activity Planner")
temperature = int(input("What is the temperature? "))
rain = input("Is it raining? (yes/no): ")
homework = input("Do you have homework? (yes/no): ")
free_time = int(input("How many minutes of free time do you have? "))
if rain == "yes":
    print("Stay inside and read a book.")
else:
    print("You can play outside.")
if temperature > 20:
    print("It is warm today.")
else:
    print("It is cold today.")
if homework == "yes":
    print("Do your homework first.")
else:
    print("You can have fun!")
if free_time > 30:
    print("You have lots of free time.")
else:
    print("You have a little free time.")