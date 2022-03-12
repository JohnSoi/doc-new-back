from sqlalchemy.orm import Session

from Platform.Class.BaseClass import BaseClass

from Models.Service import Service as ServiceModel
from Platform.Helpers import HttpQueryHelpers


class Service(BaseClass):
    AREA = 'Service'

    @staticmethod
    def get_model(new_model: bool = False):
        return ServiceModel() if new_model else ServiceModel

    @classmethod
    def search(cls, session: Session, search_str: str, filters: dict = None, only_list: bool = False):
        result = []

        query = session.query(cls.get_model()).where(cls.get_model().name.like('%{}%'.format(search_str)))
        cls._prepare_filters_in_condition([], filters)

        if query.count():
            result = [item.to_dict() for item in query]

        if only_list:
            return result

        return HttpQueryHelpers.json_response(data=result)

    @classmethod
    def _prepare_filters_in_condition(cls, conditions: list, filters: dict):
        pass
