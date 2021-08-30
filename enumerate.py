# it generate loop and index position and element name
# enumerate will generate tuples which unpacked into index(an integer) and the item(the actual value)
# the loop will print
# enumerate support in tuples dictionary string
names=['bill','mark','jeff']
for i in names:
    print(i)

print(names[0])    
print('0' ,":",'bill')


for i,j  in enumerate(names):
    print(i," :",j)

tuples=('mango','apple','grapes')
for i,j in enumerate(tuples):
    print(i,":",j)


names='python is popular'
for i,j in enumerate(names):
    print(i,":",j)

dictionay={"name":"google",
           "year":1990,
            "headquater":"sillicon valley"
           
           
           }

for i,j in enumerate(dictionay):
    print(i," : ",j)

