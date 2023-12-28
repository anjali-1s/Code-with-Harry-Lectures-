'''Write a python program to translate a message into secret code
language. use the rules below to translate normal english into
secret code language.


coding:
if the word contains atleast 3 characters,remove the first letter
and append it at the end

now append three random characters at the starting and the end
else :
     simply reverse the starting

Decoding:
if the word contains less than 3 characters , reverse it
else:
     remove 3 random characters from the start and end. Now 
     remove the last letter and append it to the begining'''


st = input("Enter a message:")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding")
coding = True if coding == "1" else False
if(coding):
     nwords = []
     for word in words:
          if(len(word) >= 3):
                r1 = "dsf"
                r2 = "jkr"
                stnew = r1+word[1:]+word[0]+r2
                nwords.append(stnew)
          else:
               nwords.append(word[::-1])
     print(" ".join(nwords))

else:
     nwords = []
     for word in words:
          if(len(word) >= 3):
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
          else:
               nwords.append(word[::-1])

          print(" ".join(nwords))
     