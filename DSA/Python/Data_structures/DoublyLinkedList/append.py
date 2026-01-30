#doubly linked list just has a pointer to previous node too in addition to next node
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None

class doublyLinkedList:
    def __init__(self):
        self.head=self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if not self.length:
            self.head=self.tail=new_node
        
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1











mydoubly_linkedlist=doublyLinkedList()
mydoubly_linkedlist.append(34)
print(mydoubly_linkedlist.head.value)