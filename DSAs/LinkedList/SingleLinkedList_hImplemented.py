class Node:
    def __init__(self, data, next):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        self.head = Node(data, self.head)

    def insert_at_index(self, index, data):
        if index == 0:
            self.head = Node(data, self.head)
            return

        if index < 0 or index > self.getLength_of_list():
            raise Exception("Index Out of Bound")

        itr = self.head

        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return

        if index < 0 or index >= self.getLength_of_list():
            raise Exception("Index Out of Bound")

        itr = self.head

        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def getLength_of_list(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def getIndex_of_value(self, value):
        index = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return index
            index += 1
            itr = itr.next

    def print(self):
        itr = self.head
        strList = ''
        while itr:
            strList += str(itr.data) + " --> "
            itr = itr.next
        print(strList)

    def getList(self):
        getLL = []
        itr = self.head
        while itr:
            getLL.append(itr.data)
            itr = itr.next
        return getLL

    def insert_values(self, dataList):
        for data in dataList:
            self.insert_at_end(data)

    def clear_existing_insert_new_values(self, dataList):
        self.head = None
        for data in dataList:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if data_after in self.getList():
            index = self.getIndex_of_value(data_after)
            self.insert_at_index(index + 1, data_to_insert)
        else:
            raise Exception("Expected value " + str(data_after) + " to be inserted after do not exist")

    def remove_by_value(self, data):
        if data in self.getList():
            index = self.getIndex_of_value(data)
            self.remove_at_index(index)
        else:
            raise Exception("Expected value " + str(data) + " to be removed do not exist")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(7)
    ll.print()
    ll.insert_at_end(9)
    ll.print()
    ll.insert_at_beginning(78)
    ll.print()
    ll.insert_at_index(1, 5)
    ll.print()
    ll.remove_at_index(2)
    ll.print()
    ll.insert_values([1, 23, 5, 6, 7])
    ll.print()
    ll.clear_existing_insert_new_values([1, 23, 5, 6, 7])
    ll.print()
    ll.insert_after_value(5, 8)
    ll.print()
    ll.remove_by_value(5)
    ll.print()
