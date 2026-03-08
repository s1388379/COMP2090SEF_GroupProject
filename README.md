# COMP2090SEF Group Project - Clinic Management System & Heap + Heap Sort

## Group Information
- Course: COMP2090SEF – Data Structures, Algorithms and Problem Solving
- Semester: Spring 2026
- Group: 65
- Members:
  - Tam Ares Ting Kwong (13883794)
  - Cheung Chak Wai Maxwell (13884490)
  - HAN Kongdongxu (13786160)


## Task 1 - Clinic Management System (Preliminary)

### Overview

This is a simple OOP-based clinic management system that models basic entities inside a hospital:

- **Patient**: personal details such as name, HKID, age, gender, and an auto-generated patient ID.
- **Doctor**: doctor name, specialty, an auto-generated doctor ID, and a list of responsible patients.
- **Appointment**: appointment date, patient ID and doctor ID.
- **UrgentCounter**: a record of the patient’s triage level and the maximum waiting time based on the 5-level emergency triage system used in Hong Kong public hospitals.





































## Task 2 – Heap (Data Structure) & Heap Sort (Algorithm)

## Overview

This folder contains the preliminary code for **Task 2** of our COMP2090SEF group project.  
We study:

- **Data structure**: Binary Heap  
- **Algorithm**: Heap Sort  

Our goal is to:

- Implement a binary heap from scratch in Python.
- Implement heap sort using the heap.
- Analyze the time complexity of heap operations and heap sort.
- Demonstrate usage with simple examples.

---

## Files (Planned)

- `heap.py`  
  - Implements a binary heap as a Python class.  
  - Planned operations:
    - `insert(value)` – insert a new element into the heap.  
    - `peek()` – return the root element (min or max depending on design).  
    - `pop()` – remove and return the root element.  
    - `heapify(iterable)` – build a heap from a list.

- `heap_sort.py`  
  - Implements **heap sort** using the heap from `heap.py`.  
  - Planned functions:
    - `heap_sort(arr)` – returns a sorted version of `arr` using heap operations.

- `test_main.py`  
  - Simple test/demo script.  
  - Will:
    - Create a heap and insert several numbers.  
    - Show the order of elements when repeatedly popping from the heap.  
    - Call `heap_sort()` on example lists and print results.

*(At pre-submission, some of these files may be placeholders and will be completed later.)*

---

## Time Complexity (To Be Discussed in Report)

We will discuss and verify in the Task 2 report:

- Heap operations:
  - `insert`: O(log n)  
  - `pop` (remove root): O(log n)  
  - `peek`: O(1)  
  - `heapify` (build heap from n elements): O(n)

- Heap sort:
  - Overall time complexity: O(n log n)

---

## How to Run (Planned)

From the project root:

```bash
cd task2_heap
python test_main.py
