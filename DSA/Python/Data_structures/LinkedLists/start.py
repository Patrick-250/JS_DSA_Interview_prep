#node container to create more nodes
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class AgentsLinkedList:
    def __init__(self):   #keep track of both head and tail.. for here i need the linkedlist to be empty on initialization
        self.head=None
        self.tail=None
        self.length=0 #to track the length of my LinkedList
      