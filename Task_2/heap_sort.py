from heap import MaxHeap

def heap_sort(arr):
    heap = MaxHeap()

    # Build heap
    for num in arr:
        heap.insert(num)

    sorted_list = []

    # Extract elements
    while not heap.is_empty():
        sorted_list.append(heap.extract_max())

    # Reverse for ascending order
    return sorted_list[::-1]


if __name__ == "__main__":
    data = [4, 1, 7, 3, 8, 5]
    print("Original data:", data)
    print("Sorted data:", heap_sort(data))
