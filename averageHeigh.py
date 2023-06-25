#################################################################
#               calculate average heigh among stundents         #
#################################################################

#receive a list of student heights
student_heights = input("Input a list of student heights ").split()
#cast to int every single height
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

cont = 0
total = 0
average = 0
#calculate the total heights and the total number of students
for h in student_heights:
    total += h
    cont += 1
#calculate the average
average = round(total / cont)

print(average)