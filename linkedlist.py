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


#driver function
if __name__ == '__main__':
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printlinkedlist()