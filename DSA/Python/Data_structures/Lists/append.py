"""
append simply add an element to the next available memory location in the array...
python allocxate  extra slots beyond the size of the array; the total of this including extra slots is called capacity
then after the slots are filled 
and u try to add another elements the whole array will be moved to a new location where all elements would fit... ;

# this is for a dynamic array. static arrays have fixed size and cant accept more elements beyond its size

"""

'''
append has a O(1) time complexity but as you already know; if we need to move an array to a new location; that would
result into O(n).
O(1) is more common especially if the size of the array is large.. so we generally say append is O(1); amortized...
'''

my_agents=["course_generator","Quiz_generator"]

#append a new agent to maybe grade the quiz... this goes at the last index n-1; 

my_agents.append("grader")




if __name__=="__main__":
    print(my_agents)



