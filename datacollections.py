# we aim at storing multiple items and the items must be of the same type.
#we have different types of data collections.
# lists, sets ,tupples ,dictionaries
# lists
#the concept is CRUD...create , read,update,delete items in alist.
# for lists we use angle brackets[].
# how to store the data is by using data collections.
#syntax.....student_name=["Sandra","patricia","phionah","Anitah".]

student_name = ["sandra","Patricia","Phionah","Anitah"]#strings
student_marks=[80, 56,78,90]#integers
data=['sandra',80,'Kamwokya']#mixed types

#access the whole type
print(student_name,type(student_name))

# accessing list items
#indexes(positive indexing)
print(student_name[0]) #Accessing the first item.
print(student_name[1])#Accessing the second item.
print(student_name[2])#Accessing the third item.
print(student_name[3])#accessing the last item.


# accessing list items
#indexes(negative indexing)
print(student_name[-4]) #Accessing the first item.
print(student_name[-3])#Accessing the second item.
print(student_name[-2])#Accessing the third item.
print(student_name[-1])#accessing the last item.

#appending (adding new items in the list.)
student_name.append("Michelle")
print(student_name)

# At a particular position
student_name.insert(2,"Faith")
print(student_name)

#assignment
print(student_name[1])
print(student_name[2])
print(student_name[3])
print(student_name[4])

