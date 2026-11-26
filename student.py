class Student():
    def __init__(self,student_name,student_id,marks,attendance_status):
        self.student_name=student_name
        self.student_id=student_id
        self.__marks=marks
        self.attendance_status=attendance_status

    def calulate_total(self):
        total=0
        for i in range(0,len(self.__marks)):
            total+=self.__marks[i]
        print(f"Total Marks:{total}")
        return total
    def calculate_average(self,total):
        average=total/len(self.__marks)
        print(f"Average Marks:{average}")
        return average

    def calculate_grade(self,average):
        if(average>=90 and average<=100):
            print("Grade A")
        elif(average>=80 and average<90):
            print("Grade B")
        elif(average>=70 and average<80):
            print("Grade C")
        elif(average>=60 and average<70):
            print("Grade D")
        elif(average>=50 and average<60):
            print("Grade E")
        elif(average<50):
            print("Grade F")
        else:
            print("Please enter a valid mark")

    def check_result(self,average):
        if average>=40:
            if self.attendance_status:
                print("You have passed the course.")
            else:
                print("You have attendance shortage. You have failed the course.")
        else:
            print("You have failed the course due to low marks.")

    def display_details(self):
        print(f"Student Name:{self.student_name}\nStudent ID:{self.student_id}\nMarks:{self.__marks}\nAttendance Status:{self.attendance_status}")


student1=Student("John Doe","AF123",[70,85.76,90,38],True)
student1.display_details()
stud1_total=student1.calulate_total()
stud1_average=student1.calculate_average(stud1_total)
student1.calculate_grade(stud1_average)
student1.check_result(stud1_average)

print("")
student2=Student("Arun Kumar","AF125",[80,85.56,80,45],True)
student2.display_details()
stud2_total=student2.calulate_total()
stud2_average=student2.calculate_average(stud2_total)
student2.calculate_grade(stud2_average)
student2.check_result(stud2_average)

print("")
student3=Student("Rose","AF127",[89,91,34,45,60],False)
student3.display_details()
stud3_total=student3.calulate_total()
stud3_average=student3.calculate_average(stud3_total)
student3.calculate_grade(stud3_average)
student3.check_result(stud3_average)

print("")
if(stud1_average>stud2_average and stud1_average>stud3_average):
    print(f"{student1.student_name} has scored the highest average marks:{stud1_average} and is the topper of the class.")
elif(stud2_average>stud1_average and stud2_average>stud3_average):
    print(f"{student2.student_name} has scored the highest average marks:{stud2_average} and is the topper of the class.")
else:
    print(f"{student3.student_name} has scored the highest average marks:{stud3_average} and is the topper of the class.")

    