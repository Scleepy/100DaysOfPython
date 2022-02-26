student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91 and score <= 100:
        result = "Outstanding"
    elif score >= 81 and score <= 90:
        result = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        result = "Acceptable"
    else:
        result = "Fail"

    student_grades[key] = result


print(student_grades)