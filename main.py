import json
import os
from datetime import date

DATA_FILE = "data.json"

def initialize_data():
    if not os.path.exists(DATA_FILE):
        # Creates an empty list in the JSON file if it doesn't exist
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

def main():
    while True:
        print("\n=============================")
        print("🔥 HABIT STREAK TRACKER 🔥")
        print("=============================")
        print("1. Log today's habit")
        print("2. View current streak")
        print("3. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            print("Logging progress... (Logic coming soon)")
        elif choice == '2':
            print("Viewing streak... (Logic coming soon)")
        elif choice == '3':
            print("Exiting tracker. Keep up the good work!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
