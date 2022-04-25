student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇

def grade(p):
    if p > 90:
        return "Outstanding"
    elif p > 80:
        return "Exceeds Expectations"
    elif p > 70:
        return "Acceptable"
    else:
        return "Fail"

for student in student_scores:
    student_grades[student] = grade(student_scores[student])

# 🚨 Don't change the code below 👇
print(student_grades)