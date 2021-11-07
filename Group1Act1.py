prelim = float(input("Enter Prelim Grade: "))
midterm = float(input("Enter Midterm Grade: "))
semi = float(input("Enter Semifinal Grade: "))
final = float(input("Enter Final Grade: "))
average = ((prelim+midterm+semi+final)/4)
print(average)

if(average >= 75):
    print("Passed")
else:
    print("Failed")

if average >= 99 and average <= 100:
    print("Rating: A")
elif average >= 90 and average <= 98:
    print("Rating: B")
elif average >= 80 and average <= 89:
    print("Rating: C")
elif average >= 71 and average <= 79:
    print("Rating: D")
elif average >= 61 and average <= 70:
    print("Rating: E")
else:
    print("Rating: F")
