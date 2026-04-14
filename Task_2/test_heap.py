from heap import MaxHeap
from heap_sort import heap_sort

def main():
    heap = MaxHeap()

    nums = [10, 5, 20, 1, 7]
    for n in nums:
        heap.insert(n)

    print("Heap array:", heap.data)
    print("Max element:", heap.peek_max())

    print("Extracted elements:")
    while not heap.is_empty():
        print(heap.extract_max(), end=" ")

    print("\n\nHeap Sort Demo:")
    data = [4, 1, 7, 3, 8, 5]
    print("Original:", data)
    print("min-heap:", heap_sort(data))


if __name__ == "__main__":
    main()
