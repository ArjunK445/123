# Lambda functions
x = lambda a,b:a+b
print("lambda functions:",x(4,5))

#map functions
num = [1,4,5,10]
x = map(lambda x:x>4,num)
print("map function:",list(x))

#filter functions
num = [1,4,5,10]
y = list(filter(lambda y:y>4,num))
print("filter function:",y)

# reduce functions
from functools import reduce
num = [1,4,5,10]
g = reduce(lambda x,y:x+y,num)
print("reduce functions:",g)

# zip functions: join two tuples together
a = ("Ram","Shyam","123")
b = ("singer","artist","numbers")
x=tuple(zip(a,b))
print("Zip functions:",x)