s="banana"
vowel="AEIOUY"
s1=0
s2=0
for i in range(len(s)):
    if s[i] not in vowel:
        s1+=(len(s)-i)
    else:
        s2+=(len(s)-i)
if s1>s2:
    print("Surat",s1)
elif s2>s1:
    print("Kevin",s2)
else:
    print("Draw")

