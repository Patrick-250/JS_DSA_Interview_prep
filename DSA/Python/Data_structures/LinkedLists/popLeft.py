#remove the element from the start; remove the head of a linkedlist
# will just add a append method to help me build a linkedlist; why not also repeat prepend for practice lols

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
        if not self.length:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        if not self.length:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def popLeft(self):
        if not self.length:
            raise Exception("sir/mam ,your linkedlist is actually empty")
        
        toberemoved=self.head
        self.head=toberemoved.next
        toberemoved.next=None #deattach the former head
        self.length-=1
        if not self.length:
            self.tail=None
        return toberemoved.value


# myLinkedList=LinkedList()
# myLinkedList.append(23)
# myLinkedList.append(55)
# # myLinkedList.append(40)
# # myLinkedList.prepend(33)
# myLinkedList.popLeft()
# # print(myLinkedList.head.value)
# # print(myLinkedList.length)
# print(myLinkedList.popLeft())