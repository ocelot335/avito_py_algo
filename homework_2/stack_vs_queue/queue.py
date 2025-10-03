class QueueNode:
    def __init__(self, value):
        self.last = None
        self.value = value


class Queue:
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self._len = 0

    def push(self, value):
        new_node = QueueNode(value)
        if self._len == 0:
            self.front_node = new_node
        else:
            self.back_node.last = new_node
        self.back_node = new_node
        self._len += 1

    def back(self):
        if self.back_node is None:
            return None
        return self.back_node.value

    def front(self):
        if self.front_node is None:
            return None
        return self.front_node.value

    def pop(self):
        if self._len == 0:
            raise IndexError("Can't pop from empty queue")
        if self._len == 1:
            self.back_node = None
        front_node = self.front_node
        self.front_node = front_node.last
        self._len -= 1
        return front_node.value

    def __len__(self):
        return self._len
