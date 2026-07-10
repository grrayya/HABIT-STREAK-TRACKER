import json
import os
from datetime import date

DATA_FILE = "data.json"

def load_data():
    """Loads data, creating a new dictionary if the file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    """Saves the dictionary back to the JSON file with nice formatting."""
    with open(DATA_FILE, "w") as file:
        # indent=4 makes the JSON file readable to humans!
        json.dump(data, file, indent=4) 

def main():
    data = load_data()
    
    # Safety Check: If the old data was a simple list, convert it to a dictionary 
    # so the new code doesn't break when reading your old saves.
    if isinstance(data, list):
        data = {"General Habit": data}
        save_data(data)

    while True:
        print("\n=============================")
        print("🔥 MULTI-HABIT TRACKER 🔥")
        print("=============================")
        print("1. Log a habit for today")
        print("2. View streaks for all habits")
        print("3. Add a new habit to track")
        print("4. Exit")
        
        try:
            choice = input("\nChoose an option: ").strip()
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Error: Please enter a valid number (1-4).")
        except ValueError as e:
            print(f"\n{e}")
            continue
        
        if choice == '1':
            if not data:
                print("\nYou aren't tracking any habits yet! Add one first (Option 3).")
                continue
            
            print("\nWhich habit did you complete?")
            # Create a numbered list of the habits
            habits = list(data.keys())
            for i, habit in enumerate(habits, 1):
                print(f"{i}. {habit}")
            
            try:
                habit_idx = int(input("\nSelect a number: ")) - 1
                if habit_idx < 0 or habit_idx >= len(habits):
                    print("Invalid selection.")
                    continue
                    
                selected_habit = habits[habit_idx]
                today = str(date.today())
                
                # Check if today is already in the list for this specific habit
                if today not in data[selected_habit]:
                    data[selected_habit].append(today)
                    save_data(data)
                    print(f"\nSuccess! Logged '{selected_habit}' for {today}.")
                else:
                    print(f"\nYou already logged '{selected_habit}' today!")
            except ValueError:
                print("\nPlease enter a valid number.")
                
        elif choice == '2':
            if not data:
                print("\nNo habits tracked yet.")
                continue
            
            print("\n📊 CURRENT STREAKS:")
            for habit, dates in data.items():
                print(f"- {habit}: {len(dates)} total days logged")
                
        elif choice == '3':
            new_habit = input("\nEnter the name of the new habit: ").strip()
            if new_habit and new_habit not in data:
                # Create a new empty list for the new habit
                data[new_habit] = []
                save_data(data)
                print(f"\nAdded '{new_habit}' to your tracker!")
            elif new_habit in data:
                print("\nYou're already tracking that habit.")
            else:
                print("\nHabit name cannot be empty.")
                
        elif choice == '4':
            print("\nExiting tracker. Keep up the good work ate it up!")
            break

if __name__ == "__main__":
    main()
