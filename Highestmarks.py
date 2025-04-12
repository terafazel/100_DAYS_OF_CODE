print("Find the highest number")
marks = [88, 76, 92, 65, 70, 85, 90, 55, 60, 79]
maximum_value = 0

for highest_marks in marks:
    if highest_marks > maximum_value:
        maximum_value = highest_marks

print("Highest mark is:", maximum_value)
