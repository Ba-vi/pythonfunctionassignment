# return values : these return a particular variable.
#approach one
# def myName():
#     return "Violah"
# myName()
# # view output
# name = myName()
# print(name)

# approach 2
# def MyName():
#     name = "Violah"
#     return name

# MyName()


# # approach 3
# def my_age(age):
#     return age
# print(f"My name is {MyName()} and iam {my_age()} years old.")
# my_age(22)

# create a function tat calculate the area of a triangle .the base and the height must be function parameters.

def area_of_triangle(base,height):
     area = (1/2)*base*height
     print(f"The area of a triangle with base {base} and height {height} is {area}")
area_of_triangle(4,6)

# without using parameters
def triangle_area():
     base = int(input("Enter the base of the triangle : "))
     height = int(input("Enter the height of the triangle : "))
     area = int((1/2)*base*height)
     print(f"The area of a triangle with base {base} and height {height} is {area}")
triangle_area()