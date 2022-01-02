student_score={"Sakil":85,"Sajib":70,"Rakib":65,"Dulal":50}

student_grade={}

for student in student_score:
    score=student_score[student]
    if score>91:
        student_grade[student]="Outstanding"
    elif score>81:
        student_grade[student]="Exceeds expectation"
    elif score>71:
        student_grade[student]="Accepted"
    else:
        student_grade[student]="Failed"
print(student_grade)