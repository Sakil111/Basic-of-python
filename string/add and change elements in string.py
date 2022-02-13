#
a="adakarbar"
print(a[5])


# to change in string first converting it into list and change it
lst=list(a)
lst[5]="d"
string="".join(lst)
print(string)

# by slicing the string and join it back
a=a[:5]+"K"+a[6:]
print(a)

