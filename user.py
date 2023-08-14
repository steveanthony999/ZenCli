import hashlib
import csv
import os


class User:
    registered_users = {}

    def __init__(self, username, password_hash):
        self.username = username
        self._password_hash = password_hash
        self.journals = []

    @classmethod
    def register(cls, username, password):
        if username in cls.registered_users:
            print("Username already exists!")
            return None
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        cls.save_user(username, password_hash)
        return cls(username, password_hash)

    @classmethod
    def login(cls, username, password):
        users = cls.load_users()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if username in users and users[username] == password_hash:
            return cls(username, password_hash)
        else:
            print("Invalid username or password!")
            return None

    @staticmethod
    def load_users():
        users = {}
        if os.path.exists("users.csv"):
            with open("users.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    users[row[0]] = row[1]
        return users

    @staticmethod
    def save_user(username, password_hash):
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password_hash])

    def verify_password(self, password):
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self._password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            # Update the password in the CSV as well
            users = self.load_users()
            users[self.username] = self._password_hash
            with open("users.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for username, password_hash in users.items():
                    writer.writerow([username, password_hash])
            print("Password changed successfully!")
        else:
            print("Incorrect old password!")
