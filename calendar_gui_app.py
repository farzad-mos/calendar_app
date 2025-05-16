
# Calendar GUI App (simplified snapshot setup)
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import pytz
import time
import threading

root = tk.Tk()
root.title("Smart Calendar App")
root.geometry("800x600")

# Frame setup
calendar_frame = ttk.Frame(root)
calendar_frame.pack(side='left', fill='y', padx=10, pady=10)

event_frame = ttk.Frame(root)
event_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

# Calendar widget
cal = Calendar(calendar_frame, selectmode='day', year=2025, month=5, day=16)
cal.pack(pady=20)

# Highlight today's date
cal.calevent_create(datetime.today(), 'Today', 'today')
cal.tag_config('today', background='lightblue', foreground='black')

# Time zone dropdown
timezone_label = ttk.Label(event_frame, text="Select Timezone:")
timezone_label.pack()

timezone_var = tk.StringVar(value='UTC')
timezone_combo = ttk.Combobox(event_frame, textvariable=timezone_var)
timezone_combo['values'] = pytz.all_timezones
timezone_combo.pack()

# Time display
time_label = ttk.Label(event_frame, text="", font=("Helvetica", 16))
time_label.pack(pady=10)

def update_time():
    while True:
        try:
            tz = pytz.timezone(timezone_var.get())
        except:
            tz = pytz.utc
        time_label.config(text=datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

threading.Thread(target=update_time, daemon=True).start()

# Simple Calculator
calc_entry = tk.Entry(event_frame, width=30)
calc_entry.pack(pady=10)

def calculate():
    try:
        result = eval(calc_entry.get())
        calc_result.config(text=f"= {result}")
    except:
        calc_result.config(text="Error")

tk.Button(event_frame, text="Calculate", command=calculate).pack()
calc_result = tk.Label(event_frame, text="", font=("Helvetica", 12))
calc_result.pack()

root.update()
root.after(1000, lambda: root.destroy())  # Close after 1s for snapshot

root.mainloop()
