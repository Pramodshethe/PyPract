
class Singly_Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self,):
        self.head = None

    def insert_to_ll_at_beginning(self, data):
        node = Singly_Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("linkd list is empty")

        itr = self.head
        ll = ''
        while itr:
            ll  += str(itr.data) + "-->"
            itr = itr.next

        print(ll)

    def insrt_at_end(self, data):
        if self.head is None:
            node = Singly_Node(data,None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Singly_Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

if __name__ == '__main__':
    linkedlist = Linked_List()
    linkedlist.insert_to_ll_at_beginning(55)
    linkedlist.insert_to_ll_at_beginning(65)
    linkedlist.print_list()
    linkedlist.insrt_at_end(77)
    linkedlist.print_list()


