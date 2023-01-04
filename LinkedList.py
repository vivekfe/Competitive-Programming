class Node(object):
    def __init__(self, value=None, next_node=None) -> None:
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = node

    def traverse(self) -> str:
        current_head = self.head
        nodes = []
        while current_head.next_node is not None:
            nodes.append(str(current_head.value))
            current_head = current_head.next_node
        nodes.append("None")
        return " -> ".join(nodes)


s = LinkedList()
s.append(5)
s.append(10)
print(s.traverse())
