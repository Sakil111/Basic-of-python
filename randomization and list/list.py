import random
names_string=input("Give me everybodies name separately: ")
name=names_string.split(",")
who_will_pay=name[random.randint(0,len(name)-1)]
print(f"{who_will_pay} will pay for everybody")

who_will_pay=random.choice(name)
print(who_will_pay +" will pay for today's meal")
#
# creat treasure map
row1=["🤌","🤌","🤌"]
row2=["🤌","🤌","🤌"]
row3=["🤌","🤌","🤌"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to keep the treasure: ")

horizontal=int(position[0])
vertical=int(position[1])
map[horizontal-1][vertical-1]="X"

print(f"{row1}\n{row2}\n{row3}")