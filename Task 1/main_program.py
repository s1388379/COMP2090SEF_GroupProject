from person import Patient, Doctor, Gender, TriageLevel
from appointment import Appointment, UrgentCounter


if __name__ == "__main__":
    patient1 = Patient("ZhangWei", "A123456(0)", 25, Gender.MALE, "P001")

    # Set doctor
    doctor1 = Doctor("Doctor Li", "Cardiology", "D001")
    doctor1.add_patient("P001")  # Releted patients

    # Have appointment
    appt = Appointment((2026, 3, 10), "P001", "D001")

    # Emergency diversion
    urgent = UrgentCounter("P001", TriageLevel.EMERGENCY)

    print(f"Patient: {patient1.name}, PID: {patient1.patient_id}")
    print(f"Doctor: {doctor1._name}, Responsible: {doctor1._responsible_patients}")
    print(f"Appintment: {appt._date}, PID: {appt.patient_id}")
    print(f"Urgent level: {urgent._triage_level.name}, Waiting limit: {urgent.get_wait_time_limit()}minutes")
