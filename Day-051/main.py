with open('file.txt','r') as f:
     print(type(f))

# move to the 10th byte in the file
     f.seek(10)

# read the next 5 bytes
     data = f.read(5)
     print(data)

# to know about the current position of the file
     current_position = f.tell()
     print(current_position)

# to truncate upto specific size we use truncate()
with open('sample.txt','w') as f1:
     f1.write('Welcome to this jagat!')
     f1.truncate(5)
     print(f1.tell())

with open('sample.txt','r') as f1:
     print(f1.read())
