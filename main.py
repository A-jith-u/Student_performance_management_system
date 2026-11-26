from student import Student


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

    