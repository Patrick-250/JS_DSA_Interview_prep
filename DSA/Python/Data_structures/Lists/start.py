# find the product of all elements in the array

def find_product(array):
    product=1 #start at one since 1 doesnt affect the product anyways lols
    for element in array:
        product=product*element  

    return product

# result=find_product([4,3,2])
# print(result)