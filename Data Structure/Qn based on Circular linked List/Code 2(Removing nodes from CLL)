'''
#Code : Removing node from Circular Linked List:
Condition : 1) Deleting head node 
            2) delete any other node 
'''
# Code 
class Node:
    def __init__(self,data=None,next=None):
        self.data = data 
        self.next = next
class Circularlinkedlist:
    def __init__(self):
        self.head = None 
        
    #Utility Function(print function):
    def printlist(self):
        itr = self.head 
        while itr:
            print(itr.data)
            itr = itr.next 
            if itr==self.head:
                break 
            
    #Insertion at Beginning:
    def insert_at_beg(self,data):
        new_node = Node(data)
        itr = self.head 
        new_node.next = self.head 
        if not self.head: # list is Empty
            new_node.next = new_node
        else:
            while itr.next!=self.head:#[list has values]
                itr = itr.next
            itr.next = new_node
            self.head = new_node
            
    #Insertion at end: 
    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            itr = self.head 
            while (itr.next!=self.head):
                itr = itr.next 
            itr.next = new_node
            new_node.next = self.head


    # Removing Node from Circular Linked list:
    def remove(self,key):
        if self.head.data == key: # Condition 1 = del head node
            itr = self.head 
            while itr.next != self.head:# End node 
                itr = itr.next 
            itr.next = self.head.next 
            self.head = self.head.next 
        else: # To delete any other node
            itr = self.head
            prev = None 
            while itr.next!=self.head : # End node 
                prev = itr 
                itr = itr.next 
                if itr.data == key:
                    prev.next = itr.next 
                    itr = itr.next 



# Execution of Program:
if __name__ == '__main__':
    cll = Circularlinkedlist()
    print("The Given Circular linked list: ")
    cll.insert_at_beg("a")
    cll.insert_at_end("b")
    cll.insert_at_end("c")
    cll.insert_at_end("d")
    cll.insert_at_end("e")
    cll.insert_at_beg("x")
    cll.printlist()
    print("Circular Linked list after removing nodes: ")
    cll.remove("a")
    cll.remove("d")
    cll.remove("x")
    cll.printlist()
