string="ajlgasjgsadglsdajkllkj"
k=3
n = len(string)
l = int(n / k)
print(l)
for i in range(0,n,3):
    sub = string[i:i+l]
    t=""
    for i in sub:
        if i in t:
            pass
        else:
            t+=i
    print(t)

