from person import Patient, Doctor, Gender, TriageLevel
from appointment import Appointment, UrgentCounter


if __name__ == "__main__":
    patient1 = Patient("ZhangWei", "A123456(0)", 25, Gender.MALE)
    print(patient1)
    
    # Set doctor
    doctor1 = Doctor("Doctor Li", "Cardiology")
    doctor1.add_patient(patient1)  # Related patients
    print(doctor1)
    print(f"Doctor ID: {doctor1.doctor_id}")
    
    # Have appointment
    appt = Appointment((2026, 3, 10), patient1.patient_id, doctor1.doctor_id)
    
    # Emergency diversion
    urgent = UrgentCounter(patient1.patient_id, TriageLevel.EMERGENCY)
    
    print(appt)
    print(urgent.describe())
    

    print(f"Patient: {patient1.name}, PID: {patient1.patient_id}")
    print(f"Doctor: {doctor1._name}, Responsible: {[p.patient_id for p in doctor1.responsible_patients]}")
    print(f"Appintment: {appt.date}, PID: {appt.patient_id}")
    print(f"Urgent level: {urgent.triage_level.name}, Waiting limit: {urgent.get_wait_time_limit()} minutes")
