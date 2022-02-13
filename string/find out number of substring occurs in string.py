string=input("Enter your text: ")
sub_string=input("Enter your substring: ")

def find_substring_number(string,substring):
    c = 0
    l = len(sub_string)
    for i in range(len(string)):
        s=string[i:i+l]
        if s==sub_string:
            c+=1
    return c
count=find_substring_number(string,sub_string)
print(count)
