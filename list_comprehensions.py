# list comprehensions are not only used for list
# we can write listcomp.. on tuples dictionary such as range()
# it allwos for loop for building list in single line
# in the place of nested for loop we can use list comprehensions

fruits=['apple','banana','mango','grapes']
add_fruits=[] # created empty list to store later append

for i in fruits:
    if "a" in i:
        add_fruits.append(i)
 

print(add_fruits)al

# list comphrension 

fruits=['apple','banana','mango','grapes']
list_comp=[ i for i in fruits if "a" in i] # syntax[itertable : itertable]

print(list_comp)
 
for i in range(10):
    if  i>5:
        print(i)
        

x=[ i for i in range(10) if i>5]  # list compr....
print(x)

fruits=['apple','banana','grapes']

upper_change=[i.capitalize() for i in fruits]
print(upper_change)

x=[ i[0] for i in fruits ]
print(x)
numbers=[1,2,3,4,5,6,7,8,10,12,25,16,19]
squares=[ i**2 for i in numbers]
print(squares)

even_number_check=[i  for i in numbers if i%2==0 ]
print(even_number_check)

string_even_message=['even' if i%2==0 else 'odd' for i in numbers]
print(numbers)
print(string_even_message)