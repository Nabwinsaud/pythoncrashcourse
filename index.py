phone_number="12-34-56-79"
for i in phone_number:
	if i=='-':
		continue
	print(i,end="")	
# name=None 
# while not name:
# 	name=input('Enter your name:')
# print('Hello ' + name)

name='coder'
user_input=input('Enter name:\n')
while user_input!=name:
	  print('username doesnot matched...infinte looop')

print('success')


