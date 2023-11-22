#list -------

marks= [95 , 88 , 55 , 89 ]
print(marks[0])
print(marks)
print(marks[0:2])

# for score in marks:
#     print(score)

marks.append(99)  # Add in marks
print(marks)

marks.insert(0,55) # insert in 0 index
print(marks)

print(99 in marks)  # check exits or not

print(len(marks))  #for check length



i  = 0
while i < len(marks):
    print(marks[i])
    i = i +1

marks.clear() # for clear all 


# Break and continue ------------

students = ["ram", "raj", "shivam", "ritik"]  # if we want at shivam use break

for student in students:
    if student == "shivam":
        break;
    print(student)


for student in students:        #shivam ko chod ka baka sab aya ga
    if student == "shivam":
        continue;
    print(student)


#Tuple --------- we can't change value in tuple

marks= (95 , 88 , 95 , 89 )
print(marks.count(95))  # kitna hai wo bata dega
print(marks.index(95))  # index bata dega


#set ---- we can't access value with index in set becz they don't give index and its unorder give output

marks= {95 , 88 , 95 , 89 }
print(marks) # doesn't give double value 


#for print

for score in marks:
    print(score)


#dictionary ---------- key and values

marks = {"english" : 1, "math":98,  "science": 8}
print(marks["math"])

marks["physics"] = 97;  # add
print(marks)

marks["physics"] =99;  # if we want change value 
print(marks)
