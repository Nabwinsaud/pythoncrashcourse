# a collection of data types which is ordered changeable
# doesnot allow duplicate element
# unique key value pair
# fast they use hashing 
# index []

company={"name":"Apple",
         "brand":"iphone",
         "year":1990,
         "revenue":"10Bilion"
         
         }

# print(company)
# print(company["name"])
# print(company['year'])
print(company.keys())
print(company.values())
print(company.items())
company.update({"name":"microsoft"})
company.pop("brand")
company.clear()
print(company)