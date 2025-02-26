# Q1
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):

        #create the node object
        new_node = Node(data)

        # linkedlsit is empty then make it the new node
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node    


