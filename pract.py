import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

def on_canvas_configure(event):
    """Update scroll region based on the size of the canvas."""
    canvas.configure(scrollregion=canvas.bbox('all'))

def populate_data(file_path, frame):
    """Read data from the file and add it to the scrollable frame."""
    with open(file_path, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        label = ttk.Label(frame, text=line.strip(), padding=5)
        label.grid(row=i, column=0, sticky="w")

# Create main window
root = ttk.Window(themename="litera")
root.title("Scrollable Data Viewer")
root.geometry("400x300")

# Create a canvas
canvas = tk.Canvas(root)
canvas.place(x=10, y=10, width=360, height=280)  # Placed with specific dimensions

# Create a scrollbar and link it to the canvas
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.place(x=370, y=10, height=280)  # Place the scrollbar next to the canvas

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Bind configuration events to dynamically adjust the scroll region
scrollable_frame.bind('<Configure>', on_canvas_configure)

# Populate the scrollable frame with data from a file
file_path = "Data/List.txt"  # Replace with your actual file path
populate_data(file_path, scrollable_frame)

root.mainloop()
