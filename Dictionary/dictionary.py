# finding the average from the dictionary
student_marks={
    "alpha":[20,30,40],
    "beta": [30,78,90],
    "gama" : [48,90,65]
}
query_name=input("enter one name: ")
output=student_marks[query_name]
score=sum(output)/len(output)
print("%.2f" % score)