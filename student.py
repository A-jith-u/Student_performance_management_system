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


