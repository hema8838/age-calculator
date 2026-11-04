Age Calculator
A simple Python Age Calculator desktop application built with
Tkinter. The program takes a date of birth (day, month, and year),
calculates the person's age using today's date, and displays the result
in a GUI window.
Features
- Simple graphical user interface.
- Separate input fields for day, month, and year.
- Calculates age in completed years.
- Checks whether the entered date is a valid calendar date.
- Rejects dates of birth that are in the future.
- Displays an error message when the date is invalid.
Technologies Used
- Python -- application logic.
- Tkinter -- graphical user interface.
- datetime (date) -- current-date and age calculations.
- Visual Studio Code (VS Code) -- development environment.
Project Structure
Age-Calculator/
├── age_calculator.py
└── README.md
Requirements
- Python 3 installed on your computer.
- Tkinter support. It is included with many standard Python
  installations. On some Linux distributions, it may need to be
  installed separately.
No third-party Python packages are required.
How to Run
1. Clone or download this repository.
2. Open the project folder in a terminal or in VS Code.
3. Run the following command:
   python age_calculator.py
   On some systems, use:
   python3 age_calculator.py
4. The Age Calculator window will open.
How to Use
1. Enter your birth day.
2. Enter your birth month.
3. Enter your birth year.
4. Click Calculate Age.
5. Your age will appear in the window.
The result is displayed in completed years and is based on the current
date.
Validation
- Invalid calendar dates (for example, an impossible day/month
  combination) show an error message.
- A future date of birth is rejected.
- If the entered values cannot be converted to integers, the program
  displays an error message.
Future Improvements
- Show age in years, months, and days.
- Add clearer input guidance and more detailed validation messages.
- Improve the interface layout and appearance.
Author
D. Hemalatha
Data Analytics
If you find this project useful, feel free to star the repository.
