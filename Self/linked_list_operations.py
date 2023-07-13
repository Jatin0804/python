class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedList:
    
    def __init__(self):
        self.head=None
        
    #Insert at beginning
    def insertAtBeginning(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    #Insert after a node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must be in Lnked list")
            return
        
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
    #Insert at end
    def insertLast(self,new_data):
        new_node=node(new_data)
        
        if self.head is None:
            self.head=new_node
            return
        
        last=self.head
        while(last.next):
            last=last.next
            
        last.next=new_node
        
    def deleteNode(self,position):
        
        if self.head is None:
            return
        
        temp=self.head
        
        if position==0:
            self.head=temp.next
            temp=None
            return
        
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
            
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next=temp.next.next
        
        temp.next=None
        temp.next=next
        
    def search(self,key):
        
        current=self.head
        
        while current is not None:
            if current.data==key:
                return True
            
            current=current.next
            
        return False
    
    def sortList(self,head):
        current=head
        index=node(None)
        
        if head is None:
            return
        else:
            while current is not None:
                #Index points to the node next to current
                index=current.next
                
                while index is not None:
                    if current.data > index.data:
                        current.data,index.data=index.data,current.data
                    
                    index=index.next
                current=current.next
                
    def printList(self):
        temp=self.head
        
        while(temp):
            print(str(temp.data)+" ",end="") 
            temp=temp.next
        
if __name__=='__main__':
    
    llist=linkedList()
    llist.insertLast(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertLast(4)
    llist.insertAfter(llist.head.next,5)
    
    print("Linked list :")
    llist.printList()
    
    print("\nAfter deleting an element :")
    llist.deleteNode(3)
    llist.printList()
    
    print()
    item_to_find=3
    if llist.search(item_to_find):
        print(str(item_to_find)+" is found.")
    else:
        print(str(item_to_find)+" is not found.")
        
    llist.sortList(llist.head)
    print("Sorted list: ")
    llist.printList()