a = 4
b = "4"
print(a is b)                                          # it checks the exact location of objects in memory.
print(a == b)                                          # it checks the values.

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)
print(l1 == l2)

str1 = "hello"
str2 = "hello"
print(str1 is str2)
print(str1 == str2)                                    # if we make a same type of and also same in values of an immutable objects then the memory assigned for it is same.