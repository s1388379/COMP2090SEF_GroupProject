from enum import Enum     #Detecting user input and convert to constant string
from typing import List


class Gender(Enum):
    MALE = "M"
    FEMALE = "F"


class TriageLevel(Enum):  # Five-tier triage system in public hospitals
    CRITICAL = 1
    EMERGENCY = 2
    URGENT = 3
    SEMI_URGENT = 4
    NON_URGENT = 5

class Patient:
    NEXT_ID = 1
    def __init__(self, name: str, hkid: str, age: int, gender: Gender, patient_id : str = None):
        self._name = name
        self._hkid = hkid
        self._age = age
        self._gender = gender
        if patient_id is None:
            self._patient_id = f"P{Patient.NEXT_ID:03d}"
            Patient.NEXT_ID += 1
        else:
            self._patient_id = patient_id

        Patient.NEXT_ID += 1

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @property
    def hkid(self):
        return self._hkid

    def __str__(self):
        return f"{self._patient_id} - {self._name} ({self._gender.value}, {self._age} yrs)"


class Doctor:
    NEXT_ID = 1

    def __init__(self, name: str, specialist: str, doctor_id: str = None):
        self._name = name
        self._specialist = specialist
        self._doctor_id = f"D{Doctor.NEXT_ID:03d}"
        Doctor.NEXT_ID += 1
        self._responsible_patients: List["Patient"] = []


    @property
    def doctor_id(self):
        return self._doctor_id

    @property
    def responsible_patients(self):
        return list(self._responsible_patients)

    @property
    def name(self):
        return self._name


    def add_patient(self, patient_id: str):
        if patient_id not in self._responsible_patients:
            self._responsible_patients.append(patient_id)

    def __str__(self):
        return f"{self._doctor_id} - Dr. {self._name} ({self._specialist})"

