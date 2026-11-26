def display_students(student_info):
    print("_______________\nStudent Record\n________________\n")
    for i in range(0,len(student_info)):
     print(student_info[i])
    print("")

def calculate_total(student_info):
     total_marks=0
     print("__________________\n The total marks \n__________________\n")
     for i in range (0,len(student_info)):
        total_marks=student_info[i]["Maths"]+student_info[i]["Science"]+student_info[i]["English"]+student_info[i]["Social"]+student_info[i]["IT"]
        print(f"Student Name:{student_info[i]["Name"]}\nTotal Marks Scored:{total_marks}\n")
        #return total_marks
     
def calculate_average(student_info):
   average={}
   print("___________________\n The average marks \n___________________\n")
   for i in range (0,len(student_info)):
    total_marks=student_info[i]["Maths"]+student_info[i]["Science"]+student_info[i]["English"]+student_info[i]["Social"]+student_info[i]["IT"]
    average_mark=total_marks/5
    average.update({student_info[i]["Name"]:average_mark})
    print(f"Student Name:{student_info[i]["Name"]}\nAverage Marks Scored:{average_mark}\n")
    

def calculate_grade(student_info):
   print("___________________\n The Grade \n___________________\n")
   for i in range(0,len(student_info)):
    total_marks=student_info[i]["Maths"]+student_info[i]["Science"]+student_info[i]["English"]+student_info[i]["Social"]+student_info[i]["IT"]
    average_mark=total_marks/5

    if(average_mark>=90 and average_mark<=100):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade A\n")
    elif(average_mark>=80 and average_mark<90):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade B\n")
    elif(average_mark>=70 and average_mark<80):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade C\n")
    elif(average_mark>=60 and average_mark<70):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade D\n")
    elif(average_mark>=50 and average_mark<60):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade E\n")
    elif(average_mark<50):
        print(f"Student Name:{student_info[i]["Name"]}\nGrade F\n")

def check_result(student_info):
   for i in range (0,len(student_info)):
      if(student_info[i]["Maths"]>=40 and student_info[i]["Science"]>=40 and student_info[i]["English"]>=40 and student_info[i]["Social"]>=40 and student_info[i]["IT"]>=40):
              if(student_info[i]["Attendance_status"]):
                print(f"{student_info[i]["Name"]} have passed the course.\n")
              else:
                 print(f"{student_info[i]["Name"]} have failed the course due to attendance shortage\n")
      else:
        print(f"{student_info[i]["Name"]} have failed the course due to low marks\n")
             
      
      

student_info=[{"Name":"Arun","student_id":"TV12","Maths":67,"Science":70,"English":87,"Social":50,"IT":45,"Attendance_status":True},
              {"Name":"Manav","student_id":"TV13","Maths":40,"Science":60,"English":77,"Social":55,"IT":65,"Attendance_status":True},
              {"Name":"Sneha","student_id":"TV14","Maths":77,"Science":86,"English":79,"Social":67,"IT":78,"Attendance_status":True},
              {"Name":"Varun","student_id":"TV15","Maths":60,"Science":50,"English":75,"Social":60,"IT":57,"Attendance_status":False},
              {"Name":"Arya","student_id":"TV16","Maths":77,"Science":83,"English":89,"Social":48,"IT":81,"Attendance_status":True}]


display_students(student_info)
calculate_total(student_info)
calculate_average(student_info)
calculate_grade(student_info)
check_result(student_info)




