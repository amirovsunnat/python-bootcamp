student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

grades = {}
for student in student_scores:
    grade = int(student_scores[student])
    if grade <= 70:
        grades[student] = "Fail"
    elif grade <= 80:
        grades[student] = "Acceptable"
    elif grade <= 90:
        grades[student] = "Exceeds Expectations"
    else:
        grades[student] = "Outstanding"
print(grades)
