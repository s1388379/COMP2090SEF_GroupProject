class MaxHeap:

    def __init__(self):
        self.data = []

    def _parent_index(self, i):
        return (i - 1) // 2

    def _left_child_index(self, i):
        return 2 * i + 1

    def _right_child_index(self, i):
        return 2 * i + 2


    def insert(self, value):

        # TODO: implement core, value, up
        pass

    def extract_max(self):

        # TODO: implement, swap root, down
        pass

    def peek_max(self):

        if not self.data:
            return None
        return self.data[0]

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    print("Current raw heap array:", heap.data)
    print("Current max:", heap.peek_max())

 

