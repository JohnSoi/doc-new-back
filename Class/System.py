from Models.Settings import Settings
from Models.Permission import Permission
from Models.Role import Role
from Models.User import User

from Platform.Helpers.HttpQuery import HttpQueryHelpers as HttpQuery
from Platform.Class.System import System as SystemPlatform
from app import engine


class System(SystemPlatform):
    AREA = 'System'

    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def add_default_data():
        try:
            engine.session.query(Permission).delete()
            engine.session.query(Role).delete()
            engine.session.query(User).delete()
            engine.session.query(Settings).delete()
            engine.session.commit()
        except:
            engine.session.rollback()

        # Settings.add_default_data()
        Permission.add_default_data()
        Role.add_default_data()
        User.add_default_data()

        return HttpQuery.json_response(success=True)

    @staticmethod
    def _save_in_db(type_load: str, types_id: int, filename: str):
        callback = {
        }

        return callback[type_load](types_id, filename)
