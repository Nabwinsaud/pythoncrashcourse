# a lambda function is anonymous function
# can take any number but can only have one expression
# anonynous means function without names

x=lambda a:a+10
print(x(2))

y=lambda a,b,c:a*b*c
print(y(1,2,3))
# def mutilpy(a,b,c):
#     return a*b*c


# def add(a):
#     return a+10

# print(add(2))


def func(a):
     return lambda y:y*a
 
multiply=func(2)
print(multiply(2)) 


numbers=[-2,-4,1,2,3]
number=-20
print(abs(number)) # absolute value

# print(number(abs))
