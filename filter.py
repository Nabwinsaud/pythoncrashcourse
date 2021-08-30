# filter function extracts elements from iterables (list tuple set) for which function return True
 # syntax filter(function ,iterable)
 # used to filter the specfic output
 
# def chek_even(a):
#     if a%2==0:
#         print('it is even') 
#     else:
#         print('not a even')
        
        


# print(chek_even(4))           

# creating function
numbers=[1,2,3,4,5,6,7,8,9,10]
def check_even(number):
    if number%2==0:
        return True
    return False

even_number=filter(check_even,numbers)
# convert_to_tuples=tuple(even_number) # convert to tuples

# print(even_number) # objects  we have to convert either in (tuples list or  set)
# print(convert_to_tuples)
print(list(even_number))


# vowels letter in check

letters=['a','b','c','d','e','g','h','i','o']

def check_vowels(letter):
    vowels=['a','e','i','o','u']
    return True if letter in vowels else False


x=filter(check_vowels,letters)

print(list(x))



 

 

