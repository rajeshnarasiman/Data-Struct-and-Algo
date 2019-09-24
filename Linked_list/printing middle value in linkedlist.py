#Node initiation
class object:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    #creating linked list
    class linkedlist:

        def __init__(self):
            self.head = None

        def push(self, new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

        def print_middle_val(self):
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data


# Driver code:
llist = linkedlist()
#passing the list and creating a linked list
a= [1,3,5,6,8,9,22,100,200]
for i in a:
    llist.push(i)
print(llist.print_middle_val())