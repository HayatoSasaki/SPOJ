# Important You should not use the sum() or len() functions in your answer. 
# You should try to replicate their functionality using what you have learnt about for loops.

student_heights = [int(i) for i in input("Input a list of student heights ").split()]

total_h = 0
total_s = 0
for sh in student_heights:
    total_h += sh
    total_s += 1

print(round(total_h / total_s))