class MaxHeap:

    def __init__(self):
        self.data = []

    def _parent_index(self, i):
        return (i - 1) // 2

    def _left_child_index(self, i):
        return 2 * i + 1

    def _right_child_index(self, i):
        return 2 * i + 2

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent_index(index)
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            left = self._left_child_index(index)
            right = self._right_child_index(index)
            largest = index

            if left < size and self.data[left] > self.data[largest]:
                largest = left

            if right < size and self.data[right] > self.data[largest]:
                largest = right

            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def extract_max(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)

        return root

    def peek_max(self):
        return self.data[0] if self.data else None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
 
