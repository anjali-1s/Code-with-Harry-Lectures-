marks = [2,3,4]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

colors = ["red","blue","green","white"]
print(colors)
print(type(colors))
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[len(colors)-2])

if "red" in colors:
     print("yes")
else:
     print("No")

print(colors)
print(colors[:])
print(colors[1:])
print(colors[1:4])
print(colors[1:4:2])

list =[i for i in range(4)]
print(list)

lst = [i*i for i in range(5) if i % 2 == 0]
print(lst)
