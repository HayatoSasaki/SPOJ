# Important you are not allowed to use the max or min functions. 
# The output words must match the example.

student_scores = [int(i) for i in input("Input a list of student scores ").split()]
print(student_scores)

s = student_scores[0]
for scores in student_scores:
    if s < scores:
        s = scores

print("The highest score in the class is: ", s)