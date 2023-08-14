import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.journals = []

    def verify_password(self, password):
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self._password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            print("Password changed successfully!")
        else:
            print("Incorrect old password!")
