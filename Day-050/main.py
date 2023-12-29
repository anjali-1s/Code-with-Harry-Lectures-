'''f = open('myfile.txt','r')
while True:
     line = f.readline()
     print(line)
     if not line:
          print(line,type(line))
          break
     print(line)
     '''

f = open('file1.txt','r')
i = 0
while True:
     i = i+1
     line = f.readline()
     print(line)
     if not line:
          break
     m1 = int(line.split(",")[0])
     m2 = int(line.split(",")[1])
     m3 = int(line.split(",")[2])

     print(f"The marks for student {i} in math is :{m1}")
     print(f"The marks for student {i} in science is :{m2}")
     print(f"The marks for student {i} in biology is :{m3}")

     print(line)


# f2 = open('files.txt','w')
# lines = ['line 1 \n', 'line 2 \n', 'line 3 \n']
# f2.writelines(lines)
# f2.close()
     