from sqlalchemy.orm import Session

from Platform.Class.BaseClass import BaseClass
from Platform.Helpers.Password import Password
from Platform.Helpers.HttpQuery import HttpQueryHelpers as HttpQuery

from Models.User import User as UserModel


class User(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return UserModel() if new_model else UserModel

    @staticmethod
    def login(session: Session, login: str, password: str):
        employee = \
            session.query(UserModel).filter(UserModel.login == login)
        if employee.count():
            employee = employee.first()
            if Password.check_hash(employee.password, password):
                return HttpQuery.json_response(data=employee.to_dict())
            else:
                return HttpQuery.json_response(error_text='Неверный пароль', success=False, field_error='password')
        else:
            return HttpQuery.json_response(error_text='Пользователь не найден', success=False, field_error='login')
