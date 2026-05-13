d={}
print(type(d))
d={1:'abc',22:'kiran',"pythonlife":1}
print(d[22])
'''
methods
get()
update()
keys()
values()
items()
'''
d={1:'abc',22:'kiran',"pythonlife":1}
print(d.get(1))
print(d.values())
print(d.items())
d.update({1111:2222})
print(d)
for i in {1:'abc',22:'kiran',"pythonlife":1}.keys():
 print(i)
for i in {1:'abc',22:'kiran',"pythonlife":1}.values():
  print(i)
for i in {1:'abc',22:'kiran',"pythonlife":1}.items():
  print(i)