 Steps to Generate an Executable File (.exe) for the Calendar App:


1. Install Required Libraries
Ensure you have all dependencies installed. Run this in your terminal:


pip install tkcalendar pytz holidays babel pyinstaller


2. Save Your Script
Save your Python code as calendar_app.py.

3. Create a .spec File (Optional but Useful)
If needed, generate and tweak a PyInstaller spec file first:


pyinstaller --name CalendarApp --onefile --noconsole calendar_app.py
--onefile: bundles into a single .exe

--noconsole: hides terminal window (optional)

--name: sets the executable name


4. Check the Output
Once complete, you’ll find your executable in the dist folder:

dist/CalendarApp.exe