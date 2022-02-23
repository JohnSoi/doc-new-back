from Models.Patient import Patient as PatientModel
from Platform.Class.BaseClass import BaseClass


class Patient(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return PatientModel() if new_model else PatientModel

    @classmethod
    def prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('type'):
                query = query.where(cls.get_model().type == filter_params.get('type'))
        return query
