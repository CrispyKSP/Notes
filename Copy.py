import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

def close_window():
    root.destroy()

def start_move(event):
    """Record the current mouse position when starting to move the window."""
    root.x = event.x
    root.y = event.y

def do_move(event):
    """Move the window based on the new mouse position."""
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")

# Create the root window
root = ttk.Window(themename="darkly")

# Remove the native window title bar
root.overrideredirect(True)

# Create a custom header frame
header_frame = ttk.Frame(root, bootstyle=PRIMARY)
header_frame.pack(fill=X)

# Add a label for the custom window title
title_label = ttk.Label(header_frame, text="Custom Window Title", font=("Helvetica", 16))
title_label.pack(side=LEFT, padx=10)

# Add a close button
close_button = ttk.Button(header_frame, text="X", command=close_window, bootstyle=DANGER)
close_button.pack(side=RIGHT, padx=10)

# Add some content below the header
content_frame = ttk.Frame(root)
content_frame.pack(fill=BOTH, expand=True)

content_label = ttk.Label(content_frame, text="Main Content Area", font=("Helvetica", 12))
content_label.pack(pady=20)

# Bind mouse events for dragging the window
header_frame.bind("<Button-1>", start_move)  # When the user clicks to start moving
header_frame.bind("<B1-Motion>", do_move)  # When the user moves the mouse while holding down the click

# Set window size and position
root.geometry("400x300+100+100")

root.mainloop()
