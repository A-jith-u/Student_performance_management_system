student_info=[{"Name":"Arun","student_id":"TV12","Maths":67,"Science":70,"English":87,"Social":50,"IT":45,"Attendance_status":True},
              {"Name":"Manav","student_id":"TV13","Maths":40,"Science":60,"English":77,"Social":55,"IT":65,"Attendance_status":True},
              {"Name":"Sneha","student_id":"TV14","Maths":77,"Science":86,"English":79,"Social":67,"IT":78,"Attendance_status":True},
              {"Name":"Varun","student_id":"TV15","Maths":60,"Science":50,"English":75,"Social":60,"IT":57,"Attendance_status":False},
              {"Name":"Arya","student_id":"TV16","Maths":77,"Science":83,"English":89,"Social":48,"IT":81,"Attendance_status":True}]


print("_______________\nStudent Record\n________________\n")
for i in range(0,len(student_info)):
    print(student_info[i])
print("")

print("The total and average marks of each student is:\n")
average={}
failed_mark=[]
passed=[]
count=0

for i in range (0,len(student_info)):
    total_marks=student_info[i]["Maths"]+student_info[i]["Science"]+student_info[i]["English"]+student_info[i]["Social"]+student_info[i]["IT"]
    average_mark=total_marks/5
    average.update({student_info[i]["Name"]:average_mark})

    print(f"Student Name:{student_info[i]["Name"]}\nTotal Marks Scored:{total_marks}\nAverage Marks Scored:{average_mark}\n")

    if(student_info[i]["Maths"]>=40 and student_info[i]["Science"]>=40 and student_info[i]["English"]>=40 and student_info[i]["Social"]>=40 and student_info[i]["IT"]>=40):
        if(student_info[i]["Attendance_status"]):
         #print(f"{student_info[i]["Name"]} have passed the course.\n")
         passed.append(student_info[i]["Name"])
         count+=1
        else:
           #print(f"{student_info[i]["Name"]} have failed the course due to attendance shortage\n")
           failed_mark.append(student_info[i]["Name"])
    else:
       # print(f"{student_info[i]["Name"]} have failed the course due to low marks\n")
       failed_mark.append(student_info[i]["Name"])


print(f"The list of students who have passed the course is:\n {passed}")
print("")
print(f"The list of students who have failed the course is:\n {failed_mark}")
print("")
print(f"The number of students who have passed the course is: {count}")

