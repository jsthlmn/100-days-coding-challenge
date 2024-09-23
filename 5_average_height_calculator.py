students_height = input("Input a lists of students heights ").split()
length_student_height = 0
sum_student_heigth = 0

for i in students_height:
    length_student_height = length_student_height + 1
print(f"There are total {length_student_height} students to be calculated")

for j in students_height:
    sum_student_heigth = sum_student_heigth + int(j)
print(f"The total of that 7 student heights is {sum_student_heigth}")

avg_height = sum_student_heigth / length_student_height

print(f"The average of students height is: {avg_height}")


# ----------OR------------


# length_studnet  = len(students_height)
# print(f"There are total {length_studnet} students to be calculated")


# for k in range(0, len(students_height)):
#     students_height[k] = int(students_height[k])

# sum_student = sum(students_height)
# print(f"The total of that 7 student heights is {sum_student}")

# average_height = sum_student / length_studnet
# print(f"The average of students height is: {average_height}")

# print(students_height)