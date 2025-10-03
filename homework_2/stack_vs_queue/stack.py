class StackNode:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.peek = None
        self._len = 0

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.peek
        self.peek = new_node
        self._len += 1

    def top(self):
        if self.peek is None:
            return None
        return self.peek.value

    def pop(self):
        if self._len == 0:
            raise IndexError("Can't pop from empty stack")

        top_node = self.peek
        self.peek = self.peek.next
        self._len -= 1
        return top_node.value

    def __len__(self):
        return self._len
