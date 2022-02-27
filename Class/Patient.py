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
    def search(cls, session: Session, search_str: str, filters: dict = None):
        result = []
        surname = search_str
        name = ''
        second_name = ''
        if ' ' in search_str:
            part_name = search_str.split(' ')
            surname = part_name[0]
            name = part_name[1] if len(part_name) else ''
            second_name = part_name[2] if len(part_name) > 2 else ''
        where_conditions_argumnets = [cls.get_model().surname.like('%{}%'.format(surname))]

        if name:
            where_conditions_argumnets.append(cls.get_model().name.like('%{}%'.format(name)))

        if second_name:
            where_conditions_argumnets.append(cls.get_model().second_name.like('%{}%'.format(second_name)))

        cls._prepare_filters_in_condition(where_conditions_argumnets, filters)
        query = session.query(cls.get_model()).where(*where_conditions_argumnets)

        if not query.count() and not name and not second_name:
            where_conditions_argumnets = [cls.get_model().surname.like('%{}%'.format(search_str)),
                                          cls.get_model().name.like('%{}%'.format(search_str)),
                                          cls.get_model().second_name.like(
                                              '%{}%'.format(search_str))]
            cls._prepare_filters_in_condition(where_conditions_argumnets, filters)
            query = session.query(cls.get_model()).where(or_(*where_conditions_argumnets))

        if query.count():
            result = [item.to_dict() for item in query]
            for item_result in result:
                item_result['value'] = '{} {} {}'.format(item_result.get('surname', ''),
                                                         item_result.get('name', ''),
                                                         item_result.get('second_name', ''))

        return HttpQueryHelpers.json_response(data=result)

    @classmethod
    def _prepare_filters_in_condition(cls, conditions: list, filters: dict):
        if filters:
            if filters.get('type'):
                conditions.append(cls.get_model().type == filters.get('type'))
            if filters.get('isActive'):
                conditions.append(cls.get_model().date_discharge == None)
