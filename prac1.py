class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkeList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node


  

    def deleteNode(self, key):  
          
       
        temp = self.head  
  
       
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  
        
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        
        if(temp == None):  
            return
  
        
        prev.next = temp.next
  
        temp = None
  
    
    


    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data)),
            temp = temp.next

if __name__=='__main__':
    llist = LinkeList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
 


print ("Linkedlist is : ")
llist.printList()

llist.deleteNode(6)
print ("Deleted Node ")
llist.printList()


