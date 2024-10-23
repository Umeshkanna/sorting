from functools import reduce


n=[1,2,3,4,9]

l=lambda x,y:x+y
print(l(2,4))

print(list(map(lambda x:2*x,n)))

print(reduce(lambda x,y: x+y,n))

print(list(filter(lambda x:x>2,n)))


m=[2,3,4,5,6]
x=[x for x in m if x%2==0]
print(x)


def add(*args,**kwargs):
    print (args)
    print(kwargs)



add(3,4,a= "kjjj",b= 5)
add(3,40,60,c="ok")
add(3)
add(g="done")
