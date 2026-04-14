from heap import MaxHeap
from person import Patient, Doctor, Gender, TriageLevel

class HospitalSystem:
    def __init__(self):
        self.waiting_heap = MaxHeap()
        self.patients = {}
        self.doctors = {}

    def add_doctor(self, name: str, specialist: str):
        doctor_id = f"D{Doctor.NEXT_ID:03d}"
        doctor = Doctor(name, specialist)
        self.doctors[doctor.doctor_id] = doctor
        return doctor

    def add_patient(self, name: str, hkid: str, age: int, gender: Gender, triage_level: TriageLevel):
        patient = Patient(name, hkid, age, gender)
        self.patients[patient.patient_id] = patient

        priority = 6 - triage_level.value
        self.waiting_heap.insert((priority, patient.patient_id, triage_level))
        return patient

    def assign_next_patient_to_doctor(self, doctor_id: str):
        if doctor_id not in self.doctors:
            return None

        if self.waiting_heap.is_empty():
            return None

        _, patient_id, triage_level = self.waiting_heap.extract_max()
        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]
        doctor.add_patient(patient)
        return patient, doctor, triage_level

    def get_waiting_list_sorted(self):
        temp_heap = MaxHeap()
        temp_heap.data = self.waiting_heap.data.copy()

        result = []
        while not temp_heap.is_empty():
            _, patient_id, triage_level = temp_heap.extract_max()
            result.append((patient_id, triage_level))
        return result
