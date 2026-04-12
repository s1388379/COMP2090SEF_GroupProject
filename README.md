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
  - Name, specialty
  - Auto-generated doctor ID
  - Responsible patient list
    
- **Appointments**
  - Appointment date
  - Patient ID and doctor ID  
    
- **Triage System (`UrgentCounter`)**
  - 5-level classification:
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
  - Private attributes (e.g. `_name`, `_hkid`, `_age`, `_gender`)
  - Controlled access using `@property` getters (and methods such as `add_patient`)
- **Class and Object Design**
  - Classes: `Patient`, `Doctor`, `Appointment`, `UrgentCounter`
- **Class Attributes**
  - Auto-increment IDs: `Patient.NEXT_ID`, `Doctor.NEXT_ID`
- **Abstraction**
  - Use of `Enum` (`Gender`, `TriageLevel`) to model fixed categories
- **Composition (Object Relationships)**
  - A `Doctor` manages multiple `Patient` objects
  - `Appointment` links patients and doctors via IDs
- **Modular Programming**
  - Code split into multiple modules:
    - `person.py`
    - `appointment.py`
    - `main_program.py`
- **Special Methods**
  - `__init__`, `__str__` for initialization and human-readable output

---

### ▶️ How to Run Task 1 Demo

```bash
cd Task_1
python main_program.py
```

This demo will:

- Create sample patients and doctors
- Assign patients to a doctor
- Create an appointment
- Demonstrate triage classification and waiting time

---

## 📊 Task 2 – Heap (Data Structure) & Heap Sort (Algorithm)

### 📖 Overview

For Task 2, we self-study:

- **Data structure**: binary **max-heap**
- **Algorithm**: **heap sort**

These topics are not covered in the course and are studied independently to extend our knowledge of data structures and algorithms.

---

## 🧠 Concept Summary

**🔹 Heap**

A **heap** is a complete binary tree that satisfies the heap property:

- **Max-heap**: parent node ≥ children
- **Min-heap**: parent node ≤ children

Heaps are commonly used to implement **priority queues**, where elements with higher priority are processed first.

**🔹 Heap Sort**

Heap sort works in two main steps:

1. Build a heap from the input data  
2. Repeatedly extract the root (maximum element)

This produces a sorted sequence.

---

## 🔗 Connection to Task 1

The heap data structure studied in Task 2 can be applied to the clinic system in Task 1.  
For example, the triage system can be improved by using a **priority queue (heap)** to automatically serve patients based on urgency level.

---

## ⚙️ Implemented Features

[`heap.py`](Task_2/heap.py)
- `insert(value)` – insert a new element and bubble up to maintain the max-heap property (O(log n))
- `extract_max()` – remove and return the maximum element and bubble down (O(log n))
- `peek_max()` – return the maximum element without removal (O(1))
- `is_empty()` – check if the heap is empty

[`heap_sort.py`](Task_2/heap_sort.py)
- Builds a `MaxHeap` by repeated `insert`
- Extracts elements to form a sorted output list (ascending order)

[`test_main.py`](Task_2/test_main.py) 
- Demonstrates:
  - Heap operations
  - Heap sort on different test cases (including empty list, single element, negatives, duplicates)

---

## ⏱ Time Complexity

| Operation     | Complexity      |
|--------------|-----------------|
| Insert        | \(O(\log n)\)   |
| Extract Max   | \(O(\log n)\)   |
| Peek          | \(O(1)\)        |
| Heap Sort     | \(O(n \log n)\) |

> Note: In this project we build the heap by repeated `insert`, so building the heap itself is \(O(n \log n)\). Using the theoretical bottom-up heap construction algorithm, it can be done in \(O(n)\), but we choose the simpler approach here.

--- 

### ▶️ How to Run Task 2 Demo

```bash
cd Task_2
python test_main.py
```

---

## ⚠️ Limitations

- The system is a simplified simulation and does not include:
  - Database storage
  - Graphical User Interface (GUI)
- The triage system is currently rule-based and not dynamically optimised
- The system is designed for demonstration and learning purposes rather than large-scale deployment

---

## 🚀 Future Improvements

- Integrate a heap-based priority queue into the triage system
- Add a GUI for better user interaction
- Implement persistent storage (file/database)
- Expand the system to include billing or medical records

---

## 📌 Academic Honesty

This project is developed by our group. External resources and AI tools (e.g., ChatGPT) were used for idea refinement, debugging, and report polishing. All code and concepts have been reviewed and understood by the group members in accordance with HKMU academic honesty policies and course project requirements.
