from person import Patient, Doctor, TriageLevel




class Appointment:
    def __init__(self, appointment_date, patient_id: str, doctor_id: str):
        self._date = appointment_date
        self._patient_id = patient_id  # import Patient.patient_id
        self._doctor_id = doctor_id  # import Doctor.doctor_id

    @property
    def patient_id(self):
        return self._patient_id


class UrgentCounter:
    def __init__(self, patient_id: str, triage_level: TriageLevel):
        self._patient_id = patient_id  #import Patient.patient_id
        self._triage_level = triage_level
        self._wait_time_limit = {
            TriageLevel.CRITICAL: 0,
            TriageLevel.EMERGENCY: 15,
            TriageLevel.URGENT: 30,
            TriageLevel.SEMI_URGENT: 60,
            TriageLevel.NON_URGENT: 120
        }[triage_level]

    @property
    def priority(self):
        return self._triage_level.value  # The smaller the number, the more urgent the situation

    def get_wait_time_limit(self):
        return self._wait_time_limit
