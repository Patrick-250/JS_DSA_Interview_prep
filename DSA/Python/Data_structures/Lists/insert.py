# insert allows you to specify the index where you wanna isnert your element
#unless the array was empty this operation is costly since we have to shift all the other indices.. O(n)
#takes 2 arguments.. the index and the element we wanna insert.. insert(index,element)

from append import my_agents
my_agents.insert(0,"topic_selector") #maybe this agent chooses a course based on user's skill level or interests

my_agents.insert(4,"grade_reviewer and reporter") #maybe this agent will review grades and submit them




if __name__=="__main__":
    print(my_agents)

