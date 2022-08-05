# Don't change the code below
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above
total_height = 0
number_of_heights = 0
for height in student_heights:
    total_height += height
    number_of_heights += 1

average_height = total_height / number_of_heights
print(round(average_height))