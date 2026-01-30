# write a python algorithm to print all keys, values in a dictionary, O(n) on this

from more_methods import keys,values,items

#use for loop to iterate through the keys

for k in keys:
    print(k)
for v in values:
    print(v)

#if we wanted to print both keys and values on the same line we would iterate through items

for k,v in items:
    print(f'{k}:{v}') # used f string for formatting...