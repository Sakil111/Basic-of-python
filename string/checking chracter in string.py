
s = input("give your text: ")
def fun2(s):
    for i in range(len(s)):
        if (s[i].isalnum()):
            return True;
            break
    return False
def fun3(s):
    for i in range(len(s)):
        if (s[i].isalpha()):
            return True;
            break
    return False
def fun4(s):
    for i in range(len(s)):
        if (s[i].isdigit()):
            return True;
            break
    return False
def fun5(s):
    for i in range(len(s)):
        if (s[i].islower()):
            return True;
            break
    return False
def fun6(s):
    for i in range(len(s)):
        if (s[i].isupper()):
            return True;
            break
    return False
num=fun2(s)
alp=fun3(s)
digit=fun4(s)
lower=fun5(s)
upper=fun6(s)
print(num)
print(alp)
print(digit)
print(lower)
print(upper)