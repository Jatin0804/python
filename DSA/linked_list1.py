class node:
    
    def __init__(self,item):
        self.item=item
        self.next=None
        
class linkedList:
    
    def __init__(self):
        self.head=None
        
if __name__=='__main__':
    
    linked_list=linkedList()
    
    #Assign item values
    linked_list.head=node(1)
    second=node(2)
    third=node(3)
    
    #Connect Nodes
    linked_list.head.next=second
    second.next=third
    
    #Print linnked list items
    while linked_list.head != None:
        print(linked_list.head.item, end =" ")
        linked_list.head=linked_list.head.next