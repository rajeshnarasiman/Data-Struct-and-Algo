#defining Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printlinkedlist(self) -> object:
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    #inserting a node in front of a node:
    def push(self,new_data):
        new_node = Node(new_data)

        if self.head = None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def update(prev_node,new_data):
        new_node = Node(new_data)

        if not prev_node:
            self.head = new_node
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head = None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


#driver function
if __name__ == '__main__':
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printlinkedlist()