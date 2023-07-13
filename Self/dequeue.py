class dequeue:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
    
    def addRear(self,item):
        self.items.append(item)
        
    def addFront(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
d=dequeue()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.items)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.items)
print(d.removeRear())
print(d.removeFront())
print(d.items)
d.addFront(55)
d.addFront(45)
print(d.items)