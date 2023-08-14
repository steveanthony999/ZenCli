import hashlib


class User:
    registered_users = {}

    def __init__(self, username, password):
        self.username = username
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.journals = []

    @classmethod
    def register(cls, username, password):
        if username in cls.registered_users:
            print("Username already exists!")
            return None
        user = cls(username, password)
        cls.registered_users[username] = user
        return user

    @classmethod
    def login(cls, username, password):
        user = cls.registered_users.get(username)
        if user and user.verify_password(password):
            return user
        return None

    def verify_password(self, password):
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self._password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            print("Password changed successfully!")
        else:
            print("Incorrect old password!")
