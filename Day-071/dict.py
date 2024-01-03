class person:
     def __init__(self,name,age):
          self.name = name
          self.agr = age
          self.verion = 1

p = person("john",30)
print(p.__dict__)

print(help(str))