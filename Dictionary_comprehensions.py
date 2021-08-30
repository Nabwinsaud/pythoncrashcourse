# similar to list comprehension but it produces dictionary instead of list



# 1.
company=['google','facebook','microsoft','apple','Netflix'] # created list

dictionary={ i:len(i) for i in company if len(i)>7 }
print(dictionary)
number={ i:i*i for i in (1,2,3,4,5)} #square of the dictionary keys
print(number)

dic1={"x":1,
      "y":2,
      "z":3
      }

# print(dic1['x'])

output={ key:value for key,value in dic1.items() if key=='z' }
print(output)

# how to merge the dictionary

d1={"coder":"nepal",
    "age":18,
    "address":"kailali"
    }

d2={"name":"mark",
    "company":"facebook",
    "established":1998
    }

d3={**d1,**d2} # * args ...kwargs**
print(d3)

set_comp={ i for i in range(5)}
print(set_comp)

# return unique elements
strings='code is fun and it is amazing'
outputs={ i.upper() for i in strings if i.isalpha() }
print(outputs)

check_even={i for i in range(1,11) if i%2==0 }
print(check_even)