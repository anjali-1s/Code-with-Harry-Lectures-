ep1 = {2:4,3:9,4:16}
ep2 = {5:25,6:36,7:49}

'''
ep1.update(ep2)
ep1.clear()
print(ep1)

empt = {}
print(empt)
'''

ep2.pop(5)
print(ep2)

ep1.popitem()
print(ep1)                                                       # popitem() will remove the last item of the dictionary.

ep3 = {3:4,4:5}
# del ep3
# print(ep3)                                                     # it will delete the entire dictionary.

del ep3[3]
print(ep3)