class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(self.head, data)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None: #if head is blank
            self.head = Node(None, data)
            return

        itr = self.head
        while itr.next: #if head not empty then go on iterating
            itr = itr.next

        #when it reaches at the last point to new node
        itr.next = Node(None, data)

if __name__ == '__main__':
    ll = linked_list()
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(40)
    ll.print_list()
    ll.insert_at_end(45)
    ll.print_list()