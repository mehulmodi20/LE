class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # adds in the front of the list
    def insert_node(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        # save current self.head as next
        node.next = self.head
        self.head = node

    # appends at the end of the list
    def append_node(self, data) -> None:
        print("adding Node")
        if self.head is None:
            self.head = Node(data)
            print(self.head)
            return
        node = self.head
        while node is not None:
            if node.next is None:
                node.next = Node(data)
                return
            node = node.next
        # return self.head

    def delete_node(self, data) -> None:
        node = self.head
        while node is not None:
            if node.data == data:
                if self.head == node:
                    self.head = node.next
                    return
                else:
                    prev_node.next = node.next
            prev_node = node
            node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))
