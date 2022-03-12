from sqlalchemy.orm import Session

from Class.Patient import Patient
from Class.Service import Service
from Class.User import User
from Platform.Helpers import HttpQueryHelpers


class Search:
    @staticmethod
    def universal_search(session: Session, search_str: str, type_search: str = None):
        users_list = User().search(session, search_str, only_list=True)
        patients_list = Patient().search(session, search_str, only_list=True)
        services_list = Service().search(session, search_str, only_list=True)

        if not type_search and len(users_list):
            type_search = 'User'
        elif not type_search and len(patients_list):
            type_search = 'Patient'
        elif not type_search and len(services_list):
            type_search = 'Service'
        else:
            type_search = 'User'

        results = {
            'user': users_list,
            'patient': patients_list,
            'services_list': services_list,
            'type': type_search
        }

        return HttpQueryHelpers.json_response(data=results)


