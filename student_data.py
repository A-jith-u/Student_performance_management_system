student_name="John Doe"
student_id="AF123"
age=20
attended_classes=True
  
marks=[70,85.76,90,38]
subjects=("Science","Maths","English","Social","IT")
subject_marks={"IT":70,"Science":85,"English":76,"social":90,"Maths":38}

print(f"_______________\nSTUDENT DETAILS\n_______________\nName:{student_name}\nID:{student_id}\nAge:{age}\nAttended classes:{attended_classes}")
print("\n")
print(f"Subjects and Marks:\n{subject_marks}")
print("")

sum=0
for i in range(0,len(marks)):
    sum=sum+marks[i]
print("Total Marks:",sum)    
print(f"Average Marks:{sum/len(marks)}")
print(f"Highest Marks:{max(marks)}")
print(f"Lowest Marks:{min(marks)}")
print("")

count=0
for i in range(0,len(marks)):
    if marks[i]>=80:
        count+=1

print(f"Number of subjects student scored more than 80 marks:{count}")


    

