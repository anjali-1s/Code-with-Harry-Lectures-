# def double(x):
#      return x*2

# print(double(5))

# The lambda functions are used as an argument for short period of time to higher-functions
double = lambda x : x * 2
print(double(5))

sum = lambda a, b : a + b
print(sum(2,3))

avg = lambda a,b,c : (a+b+c)/3
print(avg(3,4,5))


def apply(fx,value):
     return 6 + fx(value)

print(apply(double,3))
print(apply(lambda x:x*x*x,3))