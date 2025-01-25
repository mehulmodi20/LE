from llist import LinkedList


class LinkedList2(LinkedList):

    def reverseList(self):
        new_list = None
        current = self.head
        while current:
            # store next node
            next_node = current.next
            # store new_list in current_next
            current.next = new_list
            # save new_list as current node
            new_list = current
            # save next_node as current to iterate
            current = next_node
        return new_list

    def reversedList2(self):
        reversedList = LinkedList()

        while self.head:
            # save next node
            next_node = self.head.next
            self.head.next = reversedList.head
            # change next node to be current node
            self.head = next_node
        return self


ll = LinkedList2()
ll.append_node(1)
ll.append_node(2)
ll.append_node(3)
ll.append_node(4)
ll.append_node(5)
print(ll)
print(ll.reversedList2())
