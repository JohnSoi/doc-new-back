from Platform.Class.BaseClass import BaseClass

from Models import Permission as PermissionModel


class Permission(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return PermissionModel() if new_model else PermissionModel
