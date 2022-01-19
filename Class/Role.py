from Platform.Class.BaseClass import BaseClass

from Models import Role as RoleModel


class Role(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return RoleModel() if new_model else RoleModel
