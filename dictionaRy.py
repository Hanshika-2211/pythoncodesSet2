d={1:'hello guysssss','two':42567894,'blah':[1,2,3,4,5]}
d2={'blah':[1,2,3,4,5]}
print(d)
print(d.keys())
print(d.values())
d.clear()
# print(d.clear())
# print(d)
d.update(d2)
print(d)
d.pop('blah')
print(d)