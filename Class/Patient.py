from sqlalchemy import and_, or_

from Models.Patient import Patient as PatientModel
from Platform.Class.BaseClass import BaseClass
from sqlalchemy.orm import Session

from Platform.Helpers.HttpQuery import HttpQueryHelpers


class Patient(BaseClass):
    AREA = 'Patient'

    @staticmethod
    def get_model(new_model: bool = False):
        return PatientModel() if new_model else PatientModel

    @classmethod
    def prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('type'):
                query = query.where(cls.get_model().type == filter_params.get('type'))
        return query

    @classmethod
    def search(cls, session: Session, search_str: str, filters: dict = None, only_list: bool = False):
        return super().user_search(session, search_str, filters, only_list)

    @classmethod
    def _prepare_filters_in_condition(cls, conditions: list, filters: dict):
        if filters:
            if filters.get('type'):
                conditions.append(cls.get_model().type == filters.get('type'))
            if filters.get('isActive'):
                conditions.append(cls.get_model().date_discharge == None)
