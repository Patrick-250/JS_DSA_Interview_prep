from collections import defaultdict

dict=defaultdict(default_factory)
print(dict)


dict={} # key item quantity is value
# if item in cart:
#     cart[item]+=1
# else:
#     cart[item]=1

# using setdefault method

dict.setdefault(key,defaultvalue)
dict.setdefault("apple",100)
dict[apple]

#with mutable stuffs use defaultdict instead