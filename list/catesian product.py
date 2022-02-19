from itertools import product
# printing possible list from a list
print(list(product([1,2,3],repeat=2)))

# finding products from two set
print(list(product([1,2,3],[4,5,8])))

a=[1,2,9]
b=[5,8,7]
print(list(product(a,b)))

a=[[1,2,8,9],[4,7,9]]
print(list(product(*a)))
b=[[1,2,8,9],[4,7,9],[7,8,4]]
print(list(product(*b)))
# taking mulitple elements and find their catesian product as tuple
x=list(map(int,input("value").split()))
y=list(map(int,input("value").split()))
print(x,y)
print(*product(x,y))