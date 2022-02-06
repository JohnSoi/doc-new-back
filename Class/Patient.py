from Models.Patient import Patient as PatientModel
from Platform.Class.BaseClass import BaseClass


class Patient(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return PatientModel() if new_model else PatientModel
