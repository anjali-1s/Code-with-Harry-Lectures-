for i in  range(1,21):
     for j in range(1,11):
          print(i,"*",j,"=",i*j)
          if j == 10:
               print("***********************************")
               break

print("Loop ko chhodkar bahar nikal jao")

i = 1
while(i <= 10):
     print("The number is:",i)
     i = i + 1

     if(i == 11):
          continue
print("The loop has been ended!")