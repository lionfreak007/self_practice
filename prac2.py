class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    

class Linkedlist:
    def __init__(self):
        self.head = None
        self.last = None

    def push(self,new_data):
        new_node = Node(new_data)
        if (self.last == None):
            self.last = new_node
        else:
            new_node.next = self.head
        self.head = new_node



        new_node.next = self.head
        self.head = new_node



    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data))
            temp = temp.next

if __name__ == '__main__':
    llist = Linkedlist()
    llist.push(3)
    llist.push(2)
    llist.push(1)

print( "Linkedlist :")
llist.printList()



