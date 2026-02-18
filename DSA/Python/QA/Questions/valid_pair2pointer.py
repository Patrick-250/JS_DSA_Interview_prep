"""sorted array,
check if there is a pair that adds to the target.
"""
"""
arr=[2,3,5,7,10]
target=5 true but for target 50 false"""


def valid_pair2pointer(nums:list,target:int):
    i=0 #left pointer
    j=len(nums)-1

    for num in nums:
        if i+j==target:
            return True
        elif(i+j)>target:
            j-=1
        elif (i+j)<target:
            i+=1
    return False

            
print(valid_pair2pointer([2,3,5,7,10],5))


