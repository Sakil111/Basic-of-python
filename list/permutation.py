from itertools import permutations
word,num=input("Enter your words: ").split(" ")
l=list((permutations(word,int(num))))
l.sort()
for i in l:
    print("".join(i))

