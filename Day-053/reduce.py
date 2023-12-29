# reduce function applies a function to a sequence of elements and returns a single value.
# it is a part of functool module in python.

number = [1,2,3,4,5,6]
from functools import reduce
sum = reduce(lambda x , y : x + y,number)
print(sum)