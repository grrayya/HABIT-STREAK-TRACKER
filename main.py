import json
import os
from datetime import date

DATA_FILE = "data.json"

def initialize_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

def main():
    initialize_data()
    while True:
        print("\n=============================")
        print("🔥 HABIT STREAK TRACKER 🔥")
        print("=============================")
        print("1. Log today's habit")
        print("2. View current streak")
        print("3. Exit")
        
        try:
            choice = input("\nChoose an option: ").strip()
            # Input validation check
            if choice not in ['1', '2', '3']:
                raise ValueError("Error: Please enter a valid number (1, 2, or 3).")
        except ValueError as e:
            print(f"\n{e}")
            continue
        
        if choice == '1':
            try:
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                
                today = str(date.today())
                if today not in data:
                    data.append(today)
                    with open(DATA_FILE, "w") as file:
                        json.dump(data, file)
                    print(f"\nSuccess! Habit logged for {today}.")
                else:
                    print("\nYou already logged your habit today!")
            except json.JSONDecodeError:
                print("\nError: Data file is corrupted.")
                
        elif choice == '2':
            try:
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                print(f"\n🔥 You have logged {len(data)} total days! hehe ahahah")
            except json.JSONDecodeError:
                print("\nError: Data file is corrupted. not it @-@")
                
        elif choice == '3':
            print("\nExiting tracker. Keep up the good work ate it up!")
            break

if __name__ == "__main__":
    main()
