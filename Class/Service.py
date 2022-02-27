from Platform.Class.BaseClass import BaseClass

from Models.Service import Service as ServiceModel


class Service(BaseClass):
    AREA = 'Service'

    @staticmethod
    def get_model(new_model: bool = False):
        return ServiceModel() if new_model else ServiceModel
