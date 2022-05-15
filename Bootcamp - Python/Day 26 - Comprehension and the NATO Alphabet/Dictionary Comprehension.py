import pandas as pd
from random import randint

# List Comprehension | Skipped

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students = {name:randint(1,101) for name in names}
passed_students = {student:note for student,note in students.items() if note >= 60}

print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}