# List copying
list1=[1]
list2=list(list1) # /Built-in list will copy the value
list1[0]=22
print(list1)
print(list2)
# dictionary copying
dict={1:10}
dict2=dict.copy()
dict[1]=22
print(dict2)