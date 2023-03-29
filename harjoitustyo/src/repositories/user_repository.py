from entities.user import User

class UserRepository:
    def __init__(self):
        self.all_users = {}

    def get_users(self):
        return list(self.all_users.keys)

    def add_user_to_userlist(self, user):
	self.all_users[user.username] = user.password

