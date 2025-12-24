#1 write a program to store marks of 5 students in a dictionary. Each student should have 3 subjects.
students = {
    "Aman": [85, 90, 88],
    "Riya": [92, 95, 91],
    "Rahul": [70, 68, 72],
    "Neha": [60, 62, 58],
    "Karan": [45, 55, 50]
}

#2 create a function to calculate the average of marks of each student

def calculate_average(name):
    marks = students[name]   
    return sum(marks) / len(marks)

   #print(calculate_average("Aman"))

#3
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"
#4
print("Student Result:\n")

averages = {}

for name in students:
    avg = calculate_average(name)   # passing NAME, not marks
    grade = assign_grade(avg)
    averages[name] = avg

    print(f"Name: {name}, Average: {avg:.2f}, Grade: {grade}")

#5
top_scorer = max(averages, key=averages.get)

print("\nTop Scorer:")
print(f"Name: {top_scorer}, Average Marks: {averages[top_scorer]:.2f}")


