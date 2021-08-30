# basic calculator app in python
# capable of add sub mul and div


print('Enter the operator (+ - * /) ')
choose=input('Enter the operator:\n')

if choose in ('+','-','*','/'):
    num1=int(input('Enter the 1st number:\n'))
    num2=int(input('Enter the 2nd number:\n'))
    if choose =='+':
        add=num1+num2
        print('The sum of two number is {} '.format(add))
    elif choose =='-':
        sub=num1-num2
        print('The subtraction of two number is {} '.format(sub))
    elif choose =='*':
        mul=num1*num2
        print('The multiplication of two number is {} '.format(mul))
    elif choose =='/':
         div=num1/num2
         print('The division of two number is {} '.format(div))
     
    else:
        print('operator not available in this system....')
      
