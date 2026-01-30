
def two_sum(nums:list,target:int):
    dictionary={} #hash map to hold both keys and values
    for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in dictionary:
            return [dictionary[compliment],i]
        dictionary[nums[i]]=i
       

        
print(two_sum( [2,7,11,15],9))