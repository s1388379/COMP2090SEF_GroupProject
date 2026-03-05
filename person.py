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
    def __init__(self, name: str, hkid: str, age: int, gender: Gender, patient_id: str):
        self._name = name
        self._hkid = hkid
        self._age = age
        self._gender = gender
        self._patient_id = patient_id

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def name(self):
        return self._name


class Doctor:
    def __init__(self, name: str, specialist: str, doctor_id: str):
        self._name = name
        self._specialist = specialist
        self._doctor_id = doctor_id
        self._responsible_patients: List[str] = []

    @property
    def doctor_id(self):
        return self._doctor_id

    def add_patient(self, patient_id: str):
        if patient_id not in self._responsible_patients:
            self._responsible_patients.append(patient_id)
