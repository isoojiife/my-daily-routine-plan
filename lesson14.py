print("1 for Bike and 2 for car")
choice = int(input("Enter ur choice "))
if choice == 1:
    print("U have selected the bike")
    print("1.for scooter and 2 for car")
    bike_choice = int(input("Enter ur choice :"))
    if bike_choice == 1:
        print("u have selected the scooter")
elif choice == 2:
    print("U have selected the car")
    print("1.for Sedan and 2 for SUV")
    car_choice = int(input("Enter ur choice :"))
    if car_choice == 1:
        print("u have selected the Sedan")
    else:
        print("u have selected the SUV")
else:
    print("NO CAN DOOOOOOO!")
    