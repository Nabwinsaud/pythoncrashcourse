# generator is like a list comprehnsions ,except it doesnot store the list in memory
# doesnot construct list but we can iterate over to produce elements of list as required..
# unlike list comprehensions ,generators are written in with round brackets () and not square brackets []

# useful when 
# for iterating through very large range of numbers .it doesnot not store or contain

# number=[num for num in range(0,10**100000) if num%2==0 ]
import sys

# nums=(num for num in range(1,10**100000) if num%2==0 )
# # print(nums)
# # print(number)

# for i in range(10):
#     print(next(nums))


def fun():
    n=1
    print('yeid function')
    yield n
    n+=1
    print('code')
    yield n
    n+=1
    print('code is fun')
    yield n
x=fun() # return a object but doesnot start execution

# print(x)    
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
for i in fun():
    print(i)