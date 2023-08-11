#Question-1: Number Range Checker 
score = input("Enter Score: ")
Sc = float(score)

#Conditions to check
if Sc >= 0 and Sc <= 10:
    print("Low Range")
elif Sc >= 11 and Sc <= 50:
    print("Medium range")
elif Sc >= 51 and Sc <= 100:
    print("High Range")
else:
    print("Out of Range")
