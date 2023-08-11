#Question-2:Leap Year Checker
year = input("Enter year")
y = int(year)

if y % 4 == 0 or y % 400 == 0:

    print("This is leap year")
else:
    print("Not a leap year")