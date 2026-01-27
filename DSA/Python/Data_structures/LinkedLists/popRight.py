#remove the element from the end; remove the tailof a linkedlist
#this method is a lil different from the rest cz we have to loop through the list to find what points to tail since Linkedlist points to next(not prev)
# will just add a append method to help me build a linkedlist; 

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if not self.length:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def popRight(self):
        if not self.length:
            raise Exception("bruuuuh your LinkedList is empty, how u want me to remove its current tail? funny guy")
        former_tail_value=self.tail.value
        if self.length==1:
            self.head=self.tail=None
        else:
            temp_node=self.head
            while temp_node.next is not self.tail:
                temp_node=temp_node.next
            self.tail=temp_node
            self.tail.next=None
        self.length-=1
        return former_tail_value
           
            
            


my_LinkedList=LinkedList()
my_LinkedList.append(43)
my_LinkedList.append(456)
my_LinkedList.append(443)
my_LinkedList.append(33)
my_LinkedList.popRight()
print(my_LinkedList.head.value)
print(my_LinkedList.tail.value)