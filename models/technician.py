from models.user import User
from models.roles import Roles

class Technician(User):
    def __init__(self, name):
        super().__init__(name, Roles.TECHNICIAN)

    # Future: implement job viewing/updating
