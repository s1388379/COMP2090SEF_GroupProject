# COMP2090SEF Group Project – Clinic Management System & Heap + Heap Sort

## 📌 Group Information
- **Course**: COMP2090SEF – Data Structures, Algorithms and Problem Solving
- **Semester**: Spring 2026
- **Group**: 65
  
**👥 Members**:
  - Tam Ares Ting Kwong (13883794)
  - Cheung Chak Wai Maxwell (13884490)
  - HAN Kongdongxu (13786160)

---

## 🏥 Task 1 – Clinic Management System

### 📖 Problem Background

In real-world clinics and hospitals, efficient management of patients, doctors, and appointments is essential to ensure timely treatment. In particular, triage systems are used to prioritise patients based on urgency to reduce waiting time and improve patient outcomes.

This project simulates a simplified clinic management system using Object-Oriented Programming (OOP), focusing on modelling real-world entities and their relationships.

---

### 📖 System Overview

The system models the following entities:

- **Patients**
  - Name, HKID, gender, age
  - Auto-generated patient ID
    
- **Doctors**
  – Name, specialty
  - Auto-generated doctor ID
  - Responsible patient list
    
- **Appointments**
  – Appointment date
  - Patient ID and Doctor ID  
    
- **Triage System (UrgentCounter)**
  – 5-level classification:
    - Critical
    - Emergency
    - Urgent
    - Semi-urgent
    - Non-urgent
  - Each level has a predefined waiting time limit

The current version focuses on demonstrating core OOP concepts (classes, encapsulation, class attributes, composition between objects, etc.) and basic simulation of patient–doctor–appointment relationships.

---

### 📂 Main Python Files

- [`main_program.py`](Task_1/main_program.py)
- [`person.py`](Task_1/person.py)
- [`appointment.py`](Task_1/appointment.py)

---

### 🧠 OOP Concepts Demonstrated

- **Encapsulation**
  – Private attributes (`_name`, `_hkid`, etc.)
  – Controlled access using @property
- **Class and Object Design**
  – Classes: `Patient`, `Doctor`, `Appointment`, `UrgentCounter`
- **Class Attributes**
  – Auto-increment IDs (`Patient.NEXT_ID`, `Doctor.NEXT_ID`)
- **Abstraction**
  – Use of `Enum` (`Gender`, `TriageLevel`) to model fixed categories
- **Composition (Object Relationships)**
  - A `Doctor` manages multiple `Patient` objects
  - `Appointment` links patients and doctors via IDs
- **Modular Programming**
  - Code split into multiple modules:
    - `person.py`
    - `appointment.py`
    - `main_program.py`
- Special Methods
  - `__init__`, `__str__` for initialization and output formatting

---

### ▶️ How to Run Task 1 Demo

```bash
cd Task_1
python main_program.py
```

This demon will:

- Create sample patients and doctors
- Assign patients to doctor
- Create appointments
- Demonstrate triage classification and waiting time

---

## 📊 Task 2 – Heap (Data Structure) & Heap Sort (Algorithm)

### 📖 Overview

For Task 2, we self-study:

- **Data structure**: Binary **Max-Heap**
- **Algorithm**: **Heap Sort**

We implement the max-heap from scratch using a Python list, then implement heap sort that builds a heap and repeatedly extracts the maximum to produce a sorted list.

### Main Python Files

- [`heap.py`](Task_2/heap.py)
  - Implements a `MaxHeap` class using a Python list as the underlying storage.
  - Key methods:
    - `insert(value)` – insert a new element and restore the max-heap property
    - `extract_max()` – remove and return the maximum (root) element
    - `peek_max()` – return the current maximum without removing it
    - `__len__()` – number of elements in the heap
    - `is_empty()` – whether the heap is empty

- [`heap_sort.py`](Task_2/heap_sort.py)
  - Implements `heap_sort(arr)` using the `MaxHeap` class.
  - Steps:
    1. Insert all elements of `arr` into a `MaxHeap`.
    2. Repeatedly call `extract_max()` to build a descending list.
    3. Reverse the list to get ascending order.

- [`test_main.py`](Task_2/test_main.py) 
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
