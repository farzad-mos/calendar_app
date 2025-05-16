
Calendar GUI Application - Developer Notes

This Python-based calendar application was designed using the tkinter library for GUI development. It integrates several useful features tailored for educational and productivity purposes.

Key Modules Used:
-----------------
1. tkinter          - for creating the GUI interface.
2. tkcalendar       - to display calendar widgets.
3. pytz             - to handle time zones.
4. datetime         - to manage and manipulate dates and times.
5. calendar         - for calendar calculations.
6. json             - for saving notes and events persistently.
7. threading        - for running live clock updates smoothly.

Main Features Implemented:
--------------------------
1. **Add/Remove Events:**
   - Users can select a day and add event descriptions.
   - Events are stored and displayed on the calendar.
   - JSON files are used for saving events to disk.

2. **Highlight Today's Date:**
   - The calendar uses a tag to visually highlight the current day.

3. **Holiday Support by Country:**
   - A placeholder UI allows the selection of countries for holiday integration.
   - Future extensions can use APIs like `holidays` Python package for dynamic holiday listings.

4. **Editable Daily Notes:**
   - A text widget allows users to write, save, edit, or delete daily notes.
   - Notes are saved in a structured file (`notes.json`) indexed by date.

5. **Multi-calendar Support (Planned):**
   - A dropdown placeholder supports selecting various calendar systems (Jewish, Islamic, Persian, etc.).
   - Each requires custom date conversion logic, which can be added via packages like `convertdate`.

6. **Time Display with Time Zone Selection:**
   - A live digital clock shows the time based on a selected time zone from the dropdown.

7. **Built-in Simple Calculator:**
   - A basic calculator GUI is included for quick math operations.

Educational Purpose:
---------------------
This project was created for students to learn how to:
- Build multi-functional GUI applications in Python.
- Use third-party packages effectively.
- Integrate multiple tools (calendar, clock, notes, calculator) into one app.
- Implement JSON-based persistent storage.

Future Improvements:
---------------------
- Integrate APIs for real-time holidays and calendar conversions.
- Enhance UI with better styling (e.g., using ttk or custom themes).
- Support for notifications and recurring events.

Author: ChatGPT, OpenAI
