# #They are used to perform a particular task.
# # parameters act as the data/information passed within the functions.
# #area of a circle is pie*r**2. 
# # Arguments are the values passed in the function.
# # we call the function out of the function body.


# # Create a function that returns the main components of the function.
# def function_basics():
#     print(" The main components of the functions are body , parameters and arguments.")
# function_basics()  

# #create a function that returns your student name ,registration number and your age.
# def student_data():
#     student_name = input("Enter student name : ")
#     registration_number = int(input("Enter the student's registration number : "))
#     age = int(input("Enter the student's age : "))
#     print(f"My name is {student_name} of age {age} and her registration number is {registration_number}. ")

# student_data()

# # using local variables'
# def studentData():
#     student_name = "Violah"
#     student_age = 22
#     registration_number = "2024/dsc/0026"
#     print(f"I am {student_name} with registration number {registration_number} and am {student_age} years old.")

# studentData()

# # global variables
# marks = 80
# print(marks)

# parameters are the variables we pass through the function.
# Create a function that returns your student name registration number and age as parameters.
# take note of the variables.
def student_details(student_name,reg_number,age):
    student_name = "Violah"
    reg_number = 2024/26
    age = 22
    print(f"Am {student_name} with registration number {reg_number} and am {age} years old.")

student_details("violah ",2024/26,22)



