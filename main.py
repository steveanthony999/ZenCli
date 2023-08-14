from user import User


def main():
    users = {}
    current_user = None

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        if current_user:
            print("3. Create Journal Entry")
            print("4. View Journal Entries")
            print("5. Logout")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            if username in users:
                print("Username already exists!")
                continue
            password = input("Enter password: ")
            users[username] = User(username, password)
            print(f"User {username} registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users[username].verify_password(password):
                current_user = users[username]
                print(f"Logged in as {username}!")
            else:
                print("Invalid username or password!")

        elif choice == "3" and current_user:
            print("Journal entry coming soon")
            # entry = input("Enter your journal entry: ")
            # if not current_user.journals:
            #     current_user.create_journal()
            # current_user.journals[0].add_entry(entry)
            # print("Entry added successfully!")

        elif choice == "4" and current_user:
            print("Journal viewing coming soon")
            # current_user.view_journals()

        elif choice == "5" and current_user:
            current_user = None
            print("Logged out successfully!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
