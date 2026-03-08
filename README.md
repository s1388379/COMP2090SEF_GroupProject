# COMP2090SEF Group Project - Clinic Management System & Heap + Heap Sort

## Group Information
- Course: COMP2090SEF – Data Structures, Algorithms and Problem Solving
- Semester: Spring 2026
- Group number: 65
- Members:
  - Tam Ares Ting Kwong (13883794)
  - Cheung Chak Wai Maxwell (13884490)
  - HAN Kongdongxu (13786160)


## Task 1 - Clinic Management System (Preliminary)


### Overview
This is a simple OOP-based clinic management system that models basic entities inside a hospital:

- ***Patients***: name, HKID, gender, age, auto-generated patient ID
- ***Doctors***: name, specialty, auto-generated doctor ID, responsible patients
- ***Appointments***: date, patient ID, doctor ID
- ***Triage***: a 5-level emergency triage system similar to that used in Hong Kong public hospitals, with different waiting times per urgency level


### Main Python Files
- [`main_program.py`](Task_1/main_program.py)
- [`person.py`](Task_1/person.py)  
- [`appointment.py`](Task_1/appointment.py) 


### OOP Concepts Used
- Classes and objects (`Patient`, `Doctor`, `Appointment`, `UrgentCounter`, enums)
- Encapsulation via private attributes and `@property` getters/setters
- Class attributes (e.g. `Patient.NEXT_ID`, `Doctor.NEXT_ID`)
- Magic methods (`__init__`, `__str__`)
- Modular programming: multiple Python modules imported into `main_program.py` 


### How to Run Task 1 Demo
```bash
cd Task_1
python main_program.py
```


---


## Task 2 – Heap (Data Structure) & Heap Sort (Algorithm)

### Description
For Task 2, we are going to self-study the **heap** data structure and **heap sort** algorithm, which are not covered in the lecture materials in this course.


### Concept Overview
- A heap is a complete binary tree that can efficiently support priority queue operations. 
- A **max-heap** stores the largest element at the root, where every parent node is greater than or equal to its children. 
- A **min-heap** stores the smallest element at the root, where every parent node is less than or equal to its children.  
- **Heap sort** first builds a heap from the input array, then repeatedly extracts the root to produce a sorted sequence in \(O(n \log n)\) time.  


---


### Overview (Task 2 Folder)

This folder contains the preliminary code for **Task 2** of our COMP2090SEF group project.  


We study:
- **Data structure**: Max-Heap (binary heap)  
- **Algorithm**: Heap Sort  


Our goals are to:
- Implement a max-heap from scratch in Python
- Implement heap sort using the max-heap
- Analyze the time complexity of heap operations and heap sort
- Demonstrate usage with simple examples


---


## Files (Current / Planned)

- [heap.py](Task_2/heap.py)  
  - Implements a ** MaxHeap** class using as a Python list as the underlying storage
  - Methods:
    - `insert(value)` – insert a new element into the heap and restore the max-heap property  
    - `extract_max()` – remove and return the maximum (root) element
    - `peek_max()` – return the current maximum element without removing it  
    - `__len__()` – return the number of elements in the heap
    - `is_empty()` – return `True` if the heap is empty  


- [heap_sort.py](Task_2/heap_sort.py)
  - Will implement **heap sort** using the `MaxHeap` class from `heap.py`
  - Planned function:
    - `heap_sort(arr)` – build a heap from `arr`, repeatedly call `extract_max()`, and return a sorted list


- [test_main.py](Task_2/test_main.py)  (planned)
  - Simple test/demo script that will:
    - Create a `MaxHeap` and insert several numbers 
    - Print the internal heap array and the current maximum 
    - Call `heap_sort()` on example lists and print the results


---


## Time Complexity (To Be Discussed in the Report)


We will discuss and verify in the Task 2 report:


- Max-heap operations:
  - `insert`: \(O(\log n)\)  
  - `extract_max`: \(O(\log n)\)  
  - `peek_max`: \(O(1)\)


- Heap sort:
  - Building the heap from \(n\) elements: \(O(n)\)  
  - Repeated extractions: \(O(n \log n)\)  
  - Overall time complexity: \(O(n \log n)\)

    
---

## How to Run Task 2 (Preliminary)

From the project root:

```bash
cd Task_2
python heap.py       # run the MaxHeap demo
python heap_sort.py  # run the preliminary heap_sort demo
```
