# list is the data structure which can store mutiple data such as string number boolean etc 
# they are ordered and  mutuable 


fruits=['apples','banana','grapes','watermelon',1000,True]
# print(fruits)
print(fruits[0])
print(fruits[1])
fruits[0]='blackberry' #mutable
fruits.append('gauva') # it store at the last
fruits.insert(3,1000)
fruits.remove('watermelon')
fruits.sort()
fruits.pop()
fruits.clear()


print(fruits)






