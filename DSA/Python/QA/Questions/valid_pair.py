"""sorted array,
check if there is a pair that adds to the target.
"""
"""
arr=[2,3,5,7,10]
target=5 true but for target 50 false"""

def check_pairs(nums:list,target:int):
    hashmap={}
    for num in nums:
        hashmap[num]="true"
    for num in nums:
        compliment=target-num
        if compliment in hashmap:
            return True
        else:
            return False

        

print(check_pairs([2,3,5,7,10],50))

# not sure if the above solution passes all the test(no tests written lols) or if its the best one..
# feel like O(2n) dropping constants becomes O(n)... fair enough i guess... hmm two pointer technique since the array is sorted??
# well  2 pointer is still O(n)... solving with 2 pointer next....