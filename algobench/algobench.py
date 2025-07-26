import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\nWelcome to AlgoBench CLI\n")
        print("[1] Load dataset")
        print("[2] Define or import algorithm")
        print("[3] Run prediction simulation")
        print("[4] Optimize parameters")
        print("[5] Export results")
        print("[6] Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Loading dataset...")
            # Placeholder for dataset loading logic
        elif choice == '2':
            print("Defining/importing algorithm...")
            # Placeholder for algorithm logic
        elif choice == '3':
            print("Running prediction simulation...")
            # Placeholder for simulation logic
        elif choice == '4':
            print("Optimizing parameters...")
            # Placeholder for optimization logic
        elif choice == '5':
            print("Exporting results...")
            # Placeholder for export logic
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
