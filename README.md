# HabitTracker

HabitTracker is a simple command-line interface (CLI) Python application that helps users manage and track their habits. It provides a way to create new habits, mark habits as complete, and view all habits with their streaks.

## Features

- Creation of new habits with a defined periodicity (daily or weekly)
- Marking habits as complete
- Viewing all habits with their streaks
- Viewing habits with the same periodicity
- Viewing the longest run streak among all habits
- Viewing the longest streak for a specific habit
- Persistence of habit data between sessions using JSON

## Getting Started

### Prerequisites

You will need Python 3.x installed on your system to run this application.

### Running the Application

1. Clone the repository:
```
https://github.com/katleho-mokhele-iu/HabitTracker.git
```
2. Navigate to the cloned repository:
```
cd HabitTracker
```
3. Run the application:
```
python habits.py
```

### How to Use

After running the application, the command line interface will present various options. Input the number of your desired option to select it.

- `1. Create habit`: Input the name and periodicity (Daily or Weekly) of the new habit.
- `2. Complete habit`: Input the name of the habit to mark as complete.
- `3. Show habits`: Prints all habits with their streaks.
- `4. Show all habits`: Prints the names of all habits.
- `5. Show habits with same periodicity`: Input a periodicity (Daily or Weekly) to print all habits with that periodicity.
- `6. Show longest run streak`: Prints the longest run streak among all habits.
- `7. Show longest streak for a habit`: Input the name of a habit to print its longest streak.
- `8. Quit`: Exits the application.

## Testing

This application includes unit tests for the `Habit` and `HabitTracker` classes. To run the tests, uncomment the line `unittest.main()` in `main.py` and comment the line `cli()`.

## Contributing

Contributions are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is not licensed.

## Contact

For any questions or feedback, please contact the author at katleho.mokhele@iu-study.org
