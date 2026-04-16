from person import Gender, TriageLevel
from hospital import HospitalSystem

if __name__ == "__main__":
    hospital = HospitalSystem()

    # Add doctors
    doctor1 = hospital.add_doctor("Doctor Li", "Cardiology")
    doctor2 = hospital.add_doctor("Doctor Chan", "Emergency")

    # Add patient
    p1 = hospital.add_patient("ZhangWei", "A123456(0)", 25, Gender.MALE, TriageLevel.EMERGENCY)
    p2 = hospital.add_patient("Wong Mei", "B234567(1)", 60, Gender.FEMALE, TriageLevel.CRITICAL)
    p3 = hospital.add_patient("Chan Tai", "C345678(2)", 40, Gender.MALE, TriageLevel.URGENT)

    # Display Current Waiting Order
    print("Waiting list:")
    for pid, level in hospital.get_waiting_list_sorted():
        print(pid, level.name)

    # Hand them over to the doctor one by one
    print("\nAssign patients:")
    result1 = hospital.assign_next_patient_to_doctor(doctor1.doctor_id)
    print(result1)

    result2 = hospital.assign_next_patient_to_doctor(doctor2.doctor_id)
    print(result2)

    print("\nDoctor 1 patients:", [p.patient_id for p in doctor1.responsible_patients])
    print("Doctor 2 patients:", [p.patient_id for p in doctor2.responsible_patients])
