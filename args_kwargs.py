# args -paramater that will pack all the arguments into a tuple useful so that function can accept a  
# varying amount of arguments



# def add_numbers(a,b)
#     sums=a+b
#     return sums


# print(add_numbers(1,2,3))


# def add_args_numbers(*args):
#     count=0
#     for i in args:
#        count+=i
       
#     return count   


# print(add_args_numbers(1,2,3,3,4,5,6,7,8,9))

# kwargs -paramater that will pack all the arguments into a dictionary useful so that function can accept a  
# varying amount of keyword arguments



# def greet(first,last):
#     print(f'your name is  {first} {last} ')



# print(greet(first='coder',middle='from',last='nepal'))


def greet(**kwargs):
    # print('Hello ' + kwargs['first'] + " " + kwargs['middle'] +  " " +  kwargs['last'])
    print('good morning !',end='')
    for key,value in kwargs.items():
        print(value,end=" ")
    
print(greet(first='coder',middle='from',last='nepal',iscoder='yes'))    
