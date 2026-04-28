import csv
from collections import defaultdict

grades = []

# Read the CSV file
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        grades.append({
            "student": row["Student"],
            "course": row["Course"],
            "grade": int(row["Grade"])
        })

# Overall class average
total = sum(item["grade"] for item in grades)
overall_average = total / len(grades)

# Highest and lowest grades
highest_grade = max(grades, key=lambda x: x["grade"])
lowest_grade = min(grades, key=lambda x: x["grade"])

# Average grade by course
course_totals = defaultdict(list)

for item in grades:
    course_totals[item["course"]].append(item["grade"])

course_averages = {
    course: sum(scores) / len(scores)
    for course, scores in course_totals.items()
}

# Average grade by student
student_totals = defaultdict(list)

for item in grades:
    student_totals[item["student"]].append(item["grade"])

student_averages = {
    student: sum(scores) / len(scores)
    for student, scores in student_totals.items()
}

# Print results
print("Student Grade Analysis")
print("----------------------")

print(f"Overall class average: {overall_average:.2f}")

print("\nAverage grade by course:")
for course, average in course_averages.items():
    print(f"- {course}: {average:.2f}")

print("\nAverage grade by student:")
for student, average in student_averages.items():
    print(f"- {student}: {average:.2f}")

print("\nHighest grade:")
print(f"- {highest_grade['student']} in {highest_grade['course']}: {highest_grade['grade']}")

print("\nLowest grade:")
print(f"- {lowest_grade['student']} in {lowest_grade['course']}: {lowest_grade['grade']}")

# Simple insights
best_course = max(course_averages, key=course_averages.get)
lowest_course = min(course_averages, key=course_averages.get)

best_student = max(student_averages, key=student_averages.get)
lowest_student = min(student_averages, key=student_averages.get)

print("\nInsights")
print("--------")
print(f"- The course with the highest average is {best_course}.")
print(f"- The course with the lowest average is {lowest_course}.")
print(f"- The student with the highest average is {best_student}.")
print(f"- The student with the lowest average is {lowest_student}.")
