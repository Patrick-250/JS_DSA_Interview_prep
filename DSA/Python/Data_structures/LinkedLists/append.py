# this add a node at the end of a LinkedList.. O(1) time complexity.

"""
we have a LinkedList of agents course_generator,Quiz_generator; with course_generator being the head, and Quiz_generator 
being the value of head and tail respectively. 
write an algorithm to add a agents in a LinkedList one after the other.

"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return self

my_agents=LinkedList()
# print(my_agents.head)
# print(my_agents.tail)
# print(my_agents.length)
my_agents.append("course_generator")
my_agents.append("Quiz_generator")
# print(my_agents.head.value)
# print(my_agents.tail.value)
# print(my_agents.length)

            

