# COMP2090SEF Group Project – Clinic Management System & Heap + Heap Sort

## Group Information
- **Course**: COMP2090SEF – Data Structures, Algorithms and Problem Solving
- **Semester**: Spring 2026
- **Group**: 65
- **Members**:
  - Tam Ares Ting Kwong (13883794)
  - Cheung Chak Wai Maxwell (13884490)
  - HAN Kongdongxu (13786160)

---

## Task 1 – Clinic Management System

### Overview

This is a simple OOP-based clinic management system that models basic entities in a hospital:

- **Patients** – name, HKID, gender, age, auto-generated patient ID  
- **Doctors** – name, specialty, auto-generated doctor ID, responsible patients  
- **Appointments** – appointment date, patient ID, doctor ID  
- **Triage** – a 5-level emergency triage system similar to that used in Hong Kong public hospitals, with different waiting time limits per urgency level  

The current version focuses on demonstrating core OOP concepts (classes, encapsulation, class attributes, composition between objects, etc.) and basic simulation of patient–doctor–appointment relationships.

### Main Python Files

- `Task_1/main_program.py`
- `Task_1/person.py`
- `Task_1/appointment.py`

### OOP Concepts Demonstrated

- **Classes and objects**: `Patient`, `Doctor`, `Appointment`, `UrgentCounter`, `Gender`, `TriageLevel`  
- **Encapsulation**: private attributes with `@property` getters (and controlled mutation via methods such as `add_patient`)  
- **Class attributes**: `Patient.NEXT_ID`, `Doctor.NEXT_ID` for auto-generated IDs  
- **Magic methods**: `__init__`, `__str__` for object initialization and human-readable output  
- **Composition and relationships**:
  - `Doctor` keeps a list of responsible `Patient` objects
  - `Appointment` and `UrgentCounter` refer to patient and doctor IDs
- **Modular programming**: multiple Python modules (`person.py`, `appointment.py`) imported into `main_program.py`, with `if __name__ == "__main__":` as the entry point

### How to Run Task 1 Demo

```bash
cd Task_1
python main_program.py
```

This will:
- Create a demo patient and doctor
- Link the patient to the doctor
- Create an appointment
- Assign a triage level and print the waiting time information

---

## Task 2 – Heap (Data Structure) & Heap Sort (Algorithm)

### Overview

For Task 2, we self-study:

- **Data structure**: binary **max-heap** (priority queue)
- **Algorithm**: **heap sort**, based on the max-heap

We implement the max-heap from scratch using a Python list, then implement heap sort that builds a heap and repeatedly extracts the maximum to produce a sorted list.

### Main Python Files

- `Task_2/heap.py`
  - Implements a `MaxHeap` class using a Python list as the underlying storage.
  - Key methods:
    - `insert(value)` – insert a new element and restore the max-heap property
    - `extract_max()` – remove and return the maximum (root) element
    - `peek_max()` – return the current maximum without removing it
    - `__len__()` – number of elements in the heap
    - `is_empty()` – whether the heap is empty

- `Task_2/heap_sort.py`
  - Implements `heap_sort(arr)` using the `MaxHeap` class.
  - Steps:
    1. Insert all elements of `arr` into a `MaxHeap`.
    2. Repeatedly call `extract_max()` to build a descending list.
    3. Reverse the list to get ascending order.

- `Task_2/test_main.py`
  - Simple demonstration script:
    - Creates a `MaxHeap` and inserts several numbers
    - Prints the internal heap array and the current maximum
    - Calls `heap_sort()` on example lists and prints the sorted results

### Time Complexity (for report and README)

- **Max-heap operations**:
  - `insert`: \(O(\log n)\) (bubble-up)
  - `extract_max`: \(O(\log n)\) (bubble-down)
  - `peek_max`: \(O(1)\)

- **Heap sort**:
  - In our implementation: building the heap by repeated `insert` is \(O(n \log n)\), and then we do \(n\) extractions at \(O(\log n)\) each, so overall **\(O(n \log n)\)**.
  - In theory, using a bottom-up build-heap algorithm, building the heap can be done in \(O(n)\), but we use the simpler repeated-insert approach in this project.

### How to Run Task 2 Demo

From the project root:

```bash
cd Task_2
python heap.py       # run MaxHeap demo
python heap_sort.py  # run heap_sort demo
python test_main.py  # run combined tests (if implemented)
```

---

## Academic Honesty and AI Usage

We used online materials and generative AI tools (e.g. ChatGPT) for idea refinement, code review, and report polishing. All core design decisions, code, and testing have been checked and understood by our group. We follow HKMU’s academic honesty requirements and clearly declare any external assistance in the final project reports.
