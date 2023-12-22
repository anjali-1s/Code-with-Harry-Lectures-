dic = {
     20:"Anjali",
     22:"Ayushi",
     24:"Nandani",
     26:"Prity"
     }
'''
print(dic)
print(dic[26])

info = {'name':'Karan','age':19,'eligible':True}
print(info['name'])                                                            # if the value doesn't exist it throws an error.
print(info.get('eligible'))                                                    # if the value doesn't exist it gives None.
print(info.keys())
print(info.values())

for key in info.keys():
     print(info[key])
     print(f"The value corresponding to the keys {key} is {info[key]}")
'''

info = {'name':'Karan','age':19,'eligible':True}
print(info.items())

for key,value in info.items():
     print(f"The value corresponding to the key {key} is {value}")