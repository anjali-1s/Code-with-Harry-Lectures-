# create a program capable of displaying questions to the user.
#use list data type to store questions and their correct answer.
# display the final amount the person is taking home after playing the game.

Questions = [
     ["Which language was used to create fb?","python","french","javascript","PHP","None",4],

     ["Where is the capital of telangana?","Andhra","Amravati","Arunachal","shimla",2],  

     ["Who was India's first president?","A.P.J abdul kalam azad","Dr.Rajendra prasad","Mahatma Gandhi",2],

     ["Who was India's first PM?","A.P.J abdul kalam azad","Dr.Rajendra prasad","Mahatma Gandhi","pdt. JawaharLal Nehru",4]
]

levels = [1000,2000,3000,10000,20000,30000,40000,80000,320000]
money = 0

for i in range(0,len(Questions)):
     question = Questions[i]
     print(f"\n \n Question for Rs.{levels[i]}")
     print(f"a. {question[1]}               b. {question[2]}")
     print(f"c. {question[3]}               d. {question[4]}")

     reply = int(input("Enter your answer (1-4) or 0 to quit"))
     if(reply == 0):
          money = level[i-1]
          
     if(reply == question[-1]):
          print(f"Correct answer, you have won Rs. {levels[i]}")
          if(i == 4):
               money = 10000
          elif(i == 9):
               money = 320000
          elif(i == 14):
               money = 10000000
     else:
          print(f"Wrong answer")
          break

print(f"your takehome money is {money}")
