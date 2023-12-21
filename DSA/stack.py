class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def get_top(self):
        if self.top is None:
            print("Top: None")
        else:
            print(f"Top: {self.top.value}")
    
    def top_value(self):
        if self.top:
            return self.top.value
        return float("-inf")
    
    def get_height(self):
        print(f"Height is: {self.height}")
        
    def is_empty(self):
        return self.height == 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top 
        self.top = new_node
        self.height += 1
        print(f"Pushed value: {value}")
        
    def pop(self):
        if self.height == 0:  
            print("Not possible, height is 0")
            return
        
        temp = self.top 
        popped_value = self.top.value
        self.top = self.top.next
        self.height -= 1
        print(f"Popped value: {popped_value}")
        
my_stack = Stack(5)
print("Stack before push(1):") 
print("---------------------")
my_stack.print_stack()
print()
my_stack.get_top() 
my_stack.get_height()
my_stack.push(1)
print("\\nStack after push(1):")
print("---------------------")  
my_stack.print_stack()
print()
my_stack.get_top()
my_stack.get_height()  
my_stack.push(8)
print("\\nStack after push(8):")
print("---------------------")
my_stack.print_stack()
print() 
my_stack.get_top()
my_stack.get_height() 
print()
my_stack.pop()
my_stack.pop()  
my_stack.pop()
my_stack.pop()