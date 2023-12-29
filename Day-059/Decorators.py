def greet(fx):
     def mfx():
          print("Good Morning")
          fx()
          print("Thanks for using this function!")
     return mfx

@greet
def hello():
     print("Hello World")

hello()


def cheer(fx):
     def mfx():
          print("well Done!")
          fx()
          print("You have done very well!")
     return mfx
    
@cheer
def info():
     print("your marks is 400")

info()

def wish(fx):
     def mfx(*args,**kwargs):
          print("Good Morning")
          fx(*args,**kwargs)
          print("Thnx for using this function")
     return mfx

@wish
def add(n1,n2):
     print(n1+n2)

add(3,4)
