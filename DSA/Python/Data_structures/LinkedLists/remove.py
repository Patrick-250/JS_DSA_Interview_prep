#removing the node whose value is known before hand..
#why not build a brand new linkedList using append and prepend just for practicing them then add remove later..
#lets go

#declare a node to be used

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
        return self
    def prepend(self,value):
        new_node=Node(value)
        if not self.length:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return self

    def remove(self,value):
        if not self.length:
            raise Exception("bruuh your LinkedlIST empty")
        previous_node=self.head
        current_node=self.head.next
        while current_node is not None and current_node.value !=value:
            previous_node=current_node
            current_node=current_node.next
        if current_node is None:
            raise Exception("item not found bro")
        if current_node.next is None:
            self.tail=previous_node
        previous_node.next=current_node.next
        current_node.next=None

        self.length-=1
        return current_node.value







    




my_LinkedList=LinkedList()
my_LinkedList.append(23)
my_LinkedList.append(42)
my_LinkedList.prepend(45)
my_LinkedList.prepend(21)
print(my_LinkedList.length)
print(my_LinkedList.head.value)
print(my_LinkedList.tail.value)
         