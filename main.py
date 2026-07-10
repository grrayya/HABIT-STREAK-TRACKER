import json
import os
import random
from datetime import date, datetime, timedelta

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4) 

def calculate_streak(dates_list):
    """Calculates the current consecutive day streak."""
    if not dates_list:
        return 0
        
    # Convert string dates back to datetime objects and sort them
    date_objs = sorted([datetime.strptime(d, "%Y-%m-%d").date() for d in set(dates_list)])
    
    today = date.today()
    current_streak = 0
    
    # If the last logged day isn't today or yesterday, the streak is broken (0)
    if date_objs[-1] != today and date_objs[-1] != (today - timedelta(days=1)):
        return 0
        
    # Start checking backwards from the most recent logged date
    check_date = date_objs[-1]
    
    while check_date in date_objs:
        current_streak += 1
        check_date -= timedelta(days=1)
        
    return current_streak

def hype(data):
    """Checks streaks on startup and provides positive reinforcement."""
    if not data:
        print("\n[ Welcome to the tracker! Time to build some new habits GIRLLLLL. ]")
        return

    best_habit = None
    best_streak = 0

    for habit, dates in data.items():
        streak = calculate_streak(dates)
        if streak > best_streak:
            best_streak = streak
            best_habit = habit

    print("\n=============================")
    if best_streak >= 7:
        print(f"🔥 DAMN GIRL You have a {best_streak}-day streak going for '{best_habit}'! You completely ate that up.")
    elif best_streak >= 3:
        print(f"✨OOOOOOOOOOO You're on a {best_streak}-day streak for '{best_habit}'. Keep the momentum going!")
    elif best_streak > 0:
        print(f"🌱 Off to a solid start! {best_streak} days in a row for '{best_habit}'. Let's lock in mandem.")
    else:
        print("👀 Streaks are looking a little quiet... perfect day to start a new one!")
    print("=============================")


def main():
    data = load_data()
    
    # The new hype welcome screen!
    hype(data)

    while True:
        print("\n1. Log a habit for today")
        print("2. View streaks for all habits")
        print("3. Add a new habit to track")
        print("4. Exit")
        
        try:
            choice = input("\nChoose an option: ").strip()
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Error: Please enter a valid number.")
        except ValueError as e:
            print(f"\n{e}")
            continue
        
        if choice == '1':
            if not data:
                print("\nYou aren't tracking any habits yet! Add one first (Option 3).")
                continue
            
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
                
                if today not in data[selected_habit]:
                    data[selected_habit].append(today)
                    save_data(data)
                    
                    # Positive reinforcement on logging!
                    new_streak = calculate_streak(data[selected_habit])
                    hype_phrases = ["Ate it up!", "Absolute perfection.", "No days off!", "Hehe ahahah good job!"]
                    print(f"\nSuccess! Logged '{selected_habit}'. Current Streak: {new_streak} days. {random.choice(hype_phrases)}")
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
                streak = calculate_streak(dates)
                total_days = len(dates)
                print(f"- {habit}: {streak} day active streak ({total_days} total days logged)")
                
        elif choice == '3':
            new_habit = input("\nEnter the name of the new habit: ").strip()
            if new_habit and new_habit not in data:
                data[new_habit] = []
                save_data(data)
                print(f"\nAdded '{new_habit}' to your tracker!")
            elif new_habit in data:
                print("\nYou're already tracking that habit.")
            else:
                print("\nHabit name cannot be empty.")
                
        elif choice == '4':
            print("\nExiting tracker. Stay consistent!")
            break

if __name__ == "__main__":
    main()
