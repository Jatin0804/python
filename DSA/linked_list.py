class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        print("Linked list created with value:", value)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def get_head(self):
        if self.head is None:
            print("Head: None")
        else:
            print("Head:", self.head.value)

    def get_tail(self):
        if self.tail is None:
            print("Tail: None")
        else:
            print("Tail:", self.tail.value)

    def get_length(self):
        print("Length:", self.length)

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("The entry is not possible. Try again.!!!!")
            return

        if index == 0:
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
            print(value, "inserted at index 0")
            return

        if index == self.length:
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
            print(value, "inserted at index", index)
            return

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        print(value, "inserted at index", index)

    def delete_node(self, index):
        if index < 0 or index >= self.length:
            print("Deletion not possible because index value is not present.")
            return
        if self.length == 0:
            print("Deletion of node not possible because no node is available.")
            return
        if index == 0:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            del temp
            print("Deletion of starting node is done.")
            self.length -= 1
            return

        if index == self.length - 1:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                pre = self.head
                while temp.next:
                    pre = temp
                    temp = temp.next
                self.tail = pre
                self.tail.next = None
            del temp
            print("Deletion of last node is completed.")
            self.length -= 1
            return

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        del temp
        print("Deletion of node at index", index, "is done.")
        self.length -= 1
        return

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next
        middle = count // 2

        temp1 = self.head
        for _ in range(middle):
            temp1 = temp1.next

        return temp1

    def find_kth_from_end(self, k):
        if k > self.length:
            print("\nkth node from last is larger than length")
            return None
        else:
            i = self.length - k
            temp = self.head
            for _ in range(i):
                temp = temp.next
            return temp


# Example usage
# value = int(input("Enter the value: "))
my_ll = LinkedList(10)

my_ll.insert(0, 3)
my_ll.insert(0, 5)
my_ll.insert(0, 2)
my_ll.insert(0, 6)
my_ll.insert(3, 8)
my_ll.insert(1, 10)
my_ll.insert(2, 20)

print("\nLL before delete_node():")
my_ll.print_list()

my_ll.delete_node(2)
print("\nLL after delete_node() in middle:")
my_ll.print_list()

my_ll.delete_node(0)
print("\nLL after delete_node() of first node:")
my_ll.print_list()

my_ll.delete_node(2)
print("\nLL after delete_node() of last node:")
my_ll.print_list()

print("\nList before reverse : ")
my_ll.print_list()
print("\nReverse of list : ")
my_ll.reverse()
my_ll.print_list()

middle_node = my_ll.find_middle_node()
print("\nThe middle node of the list is :", middle_node.value)

kth_node = my_ll.find_kth_from_end(6)
print("\nThe kth node from last of list is :", kth_node.value)

kth_node = my_ll.find_kth_from_end(2)
print("\nThe kth node from last of list is :", kth_node.value)