#Smart Schoolday Planner
print("Smart Schoolday Planner")
print("We will ask you 3 questions to help you plan your school day.")
day  =input("What day of the week is it? ")
weather = input("What is the weather like today? ")
homework = input("Do you have any homework due today? (yes/no) ")
if day in ("Saturday", "Sunday"):
    print("It's the weekend! Enjoy your day off!")
elif weather in ("rainy", "snowy"):
    print("It's not a good day to go outside. Stay indoors and focus on your studies.")
elif homework == "yes":
else:
    print("You have homework due today. Make sure to complete it before the deadline.")
else:
    print("You don't have any homework due today. Great job staying on top of your work!")