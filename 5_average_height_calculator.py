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


# length_sutend  = len(students_height)
# sum_student = sum(students_height)
# average_height = sum_student / length_sutend
# print(f"The average of students height is: {aerage_height}")

# print(students_height)