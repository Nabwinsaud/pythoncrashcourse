 # exception handling helps us in the avoiding the error 
 # debuging the error 



try:
    a=int(input('enter the 1st number:'))
    b=int(input('enter the second number:'))
    print(a/b)
except ZeroDivisionError:
      print('cannot divide something by 0')
          

except ValueError:
    print('please type number only')
    

finally:
    print('this will execute automatically alwways...')    
    

try:
    with open('code.txt') as reader:
        print(reader.read())

except FileNotFoundError:
      print('sorry the file doesnot found !....')        

# with open('code.txt') as reader:
#         print(reader.read())


 

       
               