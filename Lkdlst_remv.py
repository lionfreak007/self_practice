class Node:
    def __init__ (self , data):
        self.data = data
        self.next = None

class LinkesList:
    def __init__ (self):
        self.head = None
        self.last = None

    def append(self, new_data):
        new_node = Node(new_data)

        if(self.head == None):
            self.head = new_node
        else:
            self.last.next = new_node
            self.last = new_node



    def deleteNode(self, val):
        temp = self.head

        if(temp is not None):
            if(temp.data == val):
                self.head = temp.next
                temp = None
                return

        while temp.data is not None:
            if(temp.data == val):
                break
            prev = temp
            temp = temp.next

        if (temp == None):

            return

        prev.next = temp.next
        temp = None






    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data)),
            temp = temp.next


if __name__ ==' __main__':
    llist = LinkesList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.append(6)

    print("Linkedlist is : ")
    llist.printList()

    llist.deleteNode(6)

    print("Linkedlist after val removal :")
    llist.printList()







