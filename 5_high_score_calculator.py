student_scores = input("Input a lists of student scores: ").split()
highest_score = 0

# Make string in list into int
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)


# -----------OR-----------
# ------Using selection sort-------

# for ind in range(len(student_scores)):
#     min_index = ind
 
#     for j in range(ind + 1, len(student_scores)):
#         # select the minimum element in every iteration
#         if student_scores[j] < student_scores[min_index]:
#             min_index = j
#     # swapping the elements to sort the array
#     (student_scores[ind], student_scores[min_index]) = (student_scores[min_index], student_scores[ind])
#     # print(student_scores)
# print(student_scores)
# print(student_scores[-1])


# -----------OR----------
# The easiest way

# student_scores.sort()
# print(student_scores)
# print(student_scores[-1])

# ----------OR----------
# The very easiest way ever
# print(max(student_scores))