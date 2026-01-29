# testing an algorithm to move all zeros in the array at the end and leaving all other elements at their original places..

def move_zeros(arr):
    zeros_temp_holder=[]
    for element in arr:
        if element==0:
            zeros_temp_holder.append(element)
    new_arr=[element for element in arr if element !=0]
    for zero in zeros_temp_holder:
        new_arr.append(zero)
    
    return new_arr

print(move_zeros([0,2,4,0,5,0,5]))


# 2 loops result in 0(2n); dropping constant gives O(n)... cant think of anything better...
# using temp values will still result in 0(n)