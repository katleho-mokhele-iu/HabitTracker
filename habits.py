import datetime
import json
import os
import unittest

# The Habit class to represent a habit
class Habit:
    # Constructor
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_dates = []  # Dates when the habit was marked as completed
        self.streak = 0  # Streak of completion

    # Method to mark a habit as completed
    def complete(self):
        self.completed_dates.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.streak += 1

# The HabitTracker class to manage habits
class HabitTracker:
    # Constructor
    def __init__(self):
        self.habits = []  # List of habits
        self.load_data()  # Load existing data from file

    # Method to create a new habit
    def create_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save_data()  # Save data after creating a new habit

    # Method to mark a habit as completed
    def complete_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.complete()
        self.save_data()  # Save data after completing a habit

    # Method to load habits data from file
    def load_data(self):
        if os.path.exists("habits.json"):
            with open("habits.json", "r") as f:
                data = json.load(f)
                for habit_data in data:
                    habit = Habit(habit_data["name"], habit_data["periodicity"])
                    habit.creation_date = habit_data["creation_date"]
                    habit.completed_dates = habit_data["completed_dates"]
                    habit.streak = habit_data["streak"]
                    self.habits.append(habit)

    # Method to save habits data to file
    def save_data(self):
        data = []
        for habit in self.habits:
            data.append(habit.__dict__)
        with open("habits.json", "w") as f:
            json.dump(data, f)

    # Method to print all habits
    def print_habits(self):
        for habit in self.habits:
            print(f"Habit: {habit.name}, Periodicity: {habit.periodicity}, Streak: {habit.streak}")

    # Method to get all habits
    def get_all_habits(self):
        return self.habits

    # Method to get habits with the same periodicity
    def get_habits_with_same_periodicity(self, periodicity):
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    # Method to get the longest run streak
    def get_longest_run_streak(self):
        longest_streak_habit = max(self.habits, key=lambda habit: habit.streak, default=None)
        return longest_streak_habit.streak if longest_streak_habit else None

    # Method to get the longest streak for a habit
    def get_longest_streak_for_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit.streak
        return None

# Command Line Interface (CLI)
def cli():
    tracker = HabitTracker()
    while True:
        # User interface
        print("1. Create habit")
        print("2. Complete habit")
        print("3. Show habits")
        print("4. Show all habits")
        print("5. Show habits with same periodicity")
        print("6. Show longest run streak")
        print("7. Show longest streak for a habit")
        print("8. Quit")
        choice = input("Enter your choice: ")
        # Actions based on user choice
        if choice == "1":
            name = input("Enter habit name: ")
            periodicity = input("Enter habit periodicity (Daily or Weekly): ")
            tracker.create_habit(name, periodicity)
        elif choice == "2":
            name = input("Enter habit name: ")
            tracker.complete_habit(name)
        elif choice == "3":
            tracker.print_habits()
        elif choice == "4":
            habits = tracker.get_all_habits()
            for habit in habits:
                print(f"Habit: {habit.name}")
        elif choice == "5":
            periodicity = input("Enter periodicity (Daily or Weekly): ")
            habits = tracker.get_habits_with_same_periodicity(periodicity)
            for habit in habits:
                print(f"Habit: {habit.name}")
        elif choice == "6":
            longest_streak = tracker.get_longest_run_streak()
            print(f"Longest run streak: {longest_streak}")
        elif choice == "7":
            name = input("Enter habit name: ")
            longest_streak = tracker.get_longest_streak_for_habit(name)
            if longest_streak is not None:
                print(f"Longest streak for {name}: {longest_streak}")
            else:
                print(f"No habit with name {name} found.")
        elif choice == "8":
            break

# Unit Testing
class TestHabit(unittest.TestCase):
    # Test complete method of Habit
    def test_complete(self):
        habit = Habit("Test Habit", "Daily")
        self.assertEqual(habit.streak, 0)
        habit.complete()
        self.assertEqual(habit.streak, 1)

class TestHabitTracker(unittest.TestCase):
    # Test create_habit method of HabitTracker
    def test_create_habit(self):
        tracker = HabitTracker()
        initial_habit_count = len(tracker.habits)
        tracker.create_habit("Test Habit", "Daily")
        self.assertEqual(len(tracker.habits), initial_habit_count + 1)


if __name__ == '__main__':
    # Uncomment the following line to run unit tests
    #unittest.main()
    # Start the command line interface
    cli()
