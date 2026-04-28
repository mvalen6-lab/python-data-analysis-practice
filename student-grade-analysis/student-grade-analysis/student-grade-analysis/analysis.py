import csv

grades = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        grades.append({
            "student": row["Student"],
            "course": row["Course"],
            "grade": int(row["Grade"])
        })

total = sum(item["grade"] for item in grades)
average = total / len(grades)

highest_grade = max(grades, key=lambda x: x["grade"])
lowest_grade = min(grades, key=lambda x: x["grade"])

print("Student Grade Analysis")
print("----------------------")
print(f"Class average: {average:.2f}")
print(f"Highest grade: {highest_grade['student']} - {highest_grade['grade']}")
print(f"Lowest grade: {lowest_grade['student']} - {lowest_grade['grade']}")
