# filter function filters the sequence of elements based on a given predicate(a function that returns boolean value) and returns a new sequence contain only the elements that meet the predicate.

l = [2,3,5,7,9]
def filter_function(a):
     return a > 4

newnewl = filter(filter_function,l)
print(list(newnewl))

number = [1,2,3,4,5,6]
def filterable_function(b):
     return b < 0

result = filter(filterable_function,number)
print(list(result))                                              # it returns an empty list.