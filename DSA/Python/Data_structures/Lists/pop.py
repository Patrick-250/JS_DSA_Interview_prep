# pop removes the last element in the array and it is O(1) and returns it

#if given an index, it removes an element of that index and returns it.. this would be O(n)

from insert import my_agents
# print(my_agents)



popped=my_agents.pop()  #removes whatever is the last elements in the array and returns it
# print(popped)
# print(my_agents) #new array after removal #['topic_selector', 'course_generator', 'Quiz_generator', 'grader']

popped_agent_on_the_index=my_agents.pop(3) # removes grader agent(3rd index) and returns it
print(popped_agent_on_the_index) #grader
print(my_agents) #even new array withb grader agents removed..




