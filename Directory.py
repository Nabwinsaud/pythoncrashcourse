# helps us to get the file folder and to get the current directory
import os

print(os.getcwd()) # get current directory
x=os.getcwd()
print(x)
y=os.listdir()
print(y)
make_dir=os.mkdir('code')
check=os.listdir()
print(check)
3 mkdir 
x=os.mkdir('pythonjs')
check=os.listdir()
print(check)

renames=os.rename('code','coder')
x=os.listdir()
print(x)
removes=os.remove('coder')
print(os.listdir())
# print(os.listdir())
import shutil
shutil.rmtree('coder')
x=os.listdir()
print(x)