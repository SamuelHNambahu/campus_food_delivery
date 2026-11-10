class OrderQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, order):
        self.items.append(order)

    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("No orders in the queue.")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)