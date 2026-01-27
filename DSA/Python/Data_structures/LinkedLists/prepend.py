# add to the start of a linkedlist



class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.head=None
        self.length=0
    def prepend(self,value):
        new_node=Node(value)
        if not self.length:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
           

my_agents=LinkedList()
my_agents.prepend("grader")
my_agents.prepend("quizzer")


    
    
