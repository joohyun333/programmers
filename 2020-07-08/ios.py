import  collections
Employee = collections.namedtuple('Person', 'name id')    # 리스트로 써도 되고!
employee1 = Employee('Dave', '4011')
print (employee1)

print (type(employee1))