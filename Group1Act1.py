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