from person import TriageLevel
 

class Appointment:
    def __init__(self, appointment_date, patient_id: str, doctor_id: str):
        self._date = appointment_date
        self._patient_id = patient_id  # import Patient.patient_id
        self._doctor_id = doctor_id  # import Doctor.doctor_id

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def doctor_id(self):
        return self._doctor_id

    @property
    def date(self):
        return self._date

    def __str__(self):
        return f"Appointment on {self._date} (Patient: {self._patient_id}, Doctor: {self._doctor_id})"


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

    @property
    def triage_level(self):
        return self._triage_level

    def get_wait_time_limit(self):
        return self._wait_time_limit

    def describe(self):
        level_desc = {
            TriageLevel.CRITICAL: "Triage I (Critical): Immediate treatment.",
            TriageLevel.EMERGENCY: "Triage II (Emergency): Within 15 minutes.",
            TriageLevel.URGENT: "Triage III (Urgent): Within 30 minutes.",
            TriageLevel.SEMI_URGENT: "Triage IV (Semi-urgent): Lower priority.",
            TriageLevel.NON_URGENT: "Triage V (Non-urgent): Lowest priority."
        }[self._triage_level]
        
        return f"{level_desc} Maximum waiting time: {self._wait_time_limit} minutes."
