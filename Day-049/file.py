# READING A FILE
# f = open('file.txt','r')
# f = open('file.txt','rt')
f = open('file.txt','rb')
'''text = f.read()
print(text)
f.close()'''

'''f2 = open('myfile.txt','w')
text = f.create()
print(text)'''

# WRITING A FILE
f3 = open('file.txt','a')
f3.write("Hello world!")
f3.close()

# WITHOUT close()
with open('myfile.txt','a') as f:
     f.write("Hey i am inside with")