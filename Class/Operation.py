from Platform.Class.BaseClass import BaseClass

from Models.Operation import Operation as OperationModel


class Operation(BaseClass):
    AREA = 'Operation'

    @staticmethod
    def get_model(new_model: bool = False):
        return OperationModel() if new_model else OperationModel
