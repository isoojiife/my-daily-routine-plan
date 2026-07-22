#library visit planner
day = input("What day is it today? ")
weather = input("What is the weather like? (sunny or rainy) ")
book_returned = input("Do you have a book to return? (yes or no) ")
  if day == Sunday:
    print("The library is closed today.")
  elif book_returned == "yes":
    print("Plan: Return your book at the library in a plasctic bag.")
  elif weather == "sunny":
    print("Plan: Walk to the library and enjoy the nice weather.")
  else:
    print("Plan: Go to the library and find a cozy spot to enjoy ur book.")