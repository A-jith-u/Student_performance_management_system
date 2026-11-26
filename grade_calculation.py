mark=float(input("Enter your average mark to check grade: "))
attended_classes=True

if(mark>=90 and mark<=100):
    print("Grade A")
elif(mark>=80 and mark<90):
    print("Grade B")
elif(mark>=70 and mark<80):
    print("Grade C")
elif(mark>=60 and mark<70):
    print("Grade D")
elif(mark>=50 and mark<60):
    print("Grade E")
elif(mark<50):
    print("Grade F")
elif(mark>100 and mark<0):
    print("Please enter a valid mark")
else:
    print("Something went wrong")

if mark>=40:
    if(attended_classes):
        print("You have passed the course.")
    else:
        print("You have attendance shortage. You have failed the course.")
else:
    print("You have failed the course due to low marks.")


        