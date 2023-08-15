from user import User
import intro
from menu import display_main_menu, display_user_menu, display_zen_garden_menu


def main():
    current_user = None
    intro.welcome()

    while True:
        if current_user:
            display_user_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                # Create Journal Entry logic
                print("Create journal entry logic coming soon")
                pass
            elif choice == "2":
                # View Journal Entries logic
                print("View journal entries logic coming soon")
                pass
            elif choice == "3":
                # Update Single Journal Entry logic
                print("Update single journal entry coming soon")
                pass
            elif choice == "4":
                # Delete Single Journal Entry logic
                print("Delete single journey entry coming soon")
                pass
            elif choice == "5":
                # View Zen Garden logic
                print("View zen garden logic coming soon")
                pass
            elif choice == "6":
                # Zen Garden Menu logic
                while True:
                    display_zen_garden_menu()
                    zen_choice = input("\nEnter your Zen Garden choice: ")
                    if zen_choice == "1":
                        # Plant a New Seed logic
                        print("Plant a new seed logic coming soon")
                        pass
                    elif zen_choice == "2":
                        zen_health = current_user.garden.calculate_score()
                        print("Zen Garden Health:")
                        print("Plants In Progress:", zen_health["In Progress"])
                        print("Plants In Final Garden:", zen_health["Final Garden"])
                        print("Plants In Trash:", zen_health["Trash"])
                        pass
                    elif zen_choice == "3":
                        break
                    # Add other Zen Garden options here
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "7":
                zen_health = current_user.garden.calculate_score()
                print("Zen Garden Health:")
                print("Plants In Progress:", zen_health["In Progress"])
                print("Plants In Final Garden:", zen_health["Final Garden"])
                print("Plants In Trash:", zen_health["Trash"])
                pass
            elif choice == "8":
                current_user = None
                print("Logged out successfully!")
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            display_main_menu()
            choice = input("\nEnter your choice: ")

            if choice == "1":
                # Register logic
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = User.register(username, password)
                if current_user:
                    print(f"User {username} registered successfully!")
                    print(f"Logged in as {username}!")
            elif choice == "2":
                # Login logic
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = User.login(username, password)
                if current_user:
                    print(f"Logged in as {username}!")
                else:
                    print("Invalid username or password!")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
