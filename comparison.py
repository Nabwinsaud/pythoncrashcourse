# compares the value such as string boolean 

a=2
b=4
print(a==b) # equals or not exactly
x=2
y=2
print(x==y)
print(x!=y) # x not equals to y ? False

a='code is fun' # short string and short integer will return True  because which is due to python machine to use
# less memory for identical objects
b= 'code is fun'
num=5
num1=5
print(num==num1)
print(a is b)
print(a==b)

print(id(a)==id(b))
x='python is most popular languges'
y='python is most popular languages'
print(x==y)
long_number=1000
long_number1=1000
print(long_number==long_number1)
x=5
y='5'
print(x is y)
print(type(x))
print(type(y))