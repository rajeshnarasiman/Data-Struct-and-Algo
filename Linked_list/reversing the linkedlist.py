class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def reverse_link(self):
        prev_node = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def push(self,new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def print_rev(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


#driver code
if __name__ == '__main__':
    llist = linkedlist()
    link_list = [1,2,3,4,5]
    for i in link_list:
        llist.push(i)

    llist.print_rev()

    # llist.reverse_link()
    #
    # llist.print_rev()