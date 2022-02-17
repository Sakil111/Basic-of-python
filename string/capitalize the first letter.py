def capitalize(n):
    for x in n[:].split():
        n=n.replace(x,x.capitalize())
        return n

n=input("Enter your name: ")
s=capitalize(n)
print(s)

