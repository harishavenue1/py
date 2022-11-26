class Node:
    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def printDll(self):
        itr = self.head
        strDll = ''
        while itr:
            strDll += str(itr.data) + " --> "
            itr = itr.next
        print(strDll)

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return
        else:
            node = Node(data, self.head, None)
            self.head.previous = node
            self.head = node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if index == count:
                node = Node(data, itr, itr.previous)
                itr.previous.next = node
                node.next = itr
            itr = itr.next
            count += 1


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_beginning(5)
    dll.printDll()
