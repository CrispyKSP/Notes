import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Text, Entry, messagebox
from ttkbootstrap.constants import *
import tkinter as tk

def delete_bist(bist, canvas):
    """Delete items from bist list on the canvas."""
    for i in bist:
        canvas.delete(i)

def delete_cist(cist):
    """Destroy widgets in the cist list."""
    for i in cist:
        i.destroy()

def populate_data(file_path, frame):
    """Read data from the file and add paragraphs as editable Text widgets."""
    with open(file_path, 'r') as file:
        data = file.read()  # Read the entire file content at once

    paragraphs = data.split("\n\n")  # Split the content into paragraphs using double newlines

    for i, paragraph in enumerate(paragraphs):
        # Create Text widget for each paragraph
        text_box = Text(frame, wrap="word", height=100, width=60)  # Larger height for paragraphs
        text_box.insert("1.0", paragraph.strip())  # Insert the paragraph into the Text widget
        text_box.grid(row=i, column=0, sticky="w", padx=5, pady=5)  # Place the Text widget with padding

        # Optional: Disable Text widget initially to prevent editing, can be enabled on demand
        text_box.config(state="normal")  # Or set to "disabled" if you want read-only initially

def populate(file_path, frame):
    """Read data from the file and add it to the scrollable frame."""
    with open(file_path, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        label = ttk.Label(frame, text=line.strip(), padding=2)
        label.grid(row=i, column=0, sticky="w")

def save_note(file_path, frame):
    """Save the contents of the editable Text widgets to the file."""
    all_text = []
    for widget in frame.winfo_children():
        if isinstance(widget, Text):
            content = widget.get("1.0", tk.END).strip()
            all_text.append(content + "\n")  # Add the content of the Text widget to the list

    with open(file_path, 'w') as file:
        file.writelines(all_text)  # Save all content back to the file

def old_note(window, canvas, name):
    """Open existing note or create a new one."""
    note_name = name.get()

    try:
        with open("List.txt", "a") as file:
            file.write(note_name + "\n")

    except Exception as e:
        print("Error at line 11 : ", e)

    Note = ttk.Window(themename="darkly")
    Note.title(note_name)
    Note.geometry("400x300")
    Note.resizable(False, False)

    boanvas = Canvas(Note, width=400, height=300)
    boanvas.place(x=0, y=0, width=400, height=300)

    scrollbar = ttk.Scrollbar(Note, orient=VERTICAL, command=boanvas.yview)
    scrollbar.place(x=380, y=0, height=300)
    boanvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind('<Configure>', lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    # Populate the scrollable frame with editable text widgets from the file
    file_path = "Data/" + note_name + ".txt"
    populate_data(file_path, scrollable_frame)

    # Save button to save edited note
    save_button = ttk.Button(Note, text="Save", command=lambda: save_note(file_path, scrollable_frame))
    save_button.place(x=170, y=270)

    Note.mainloop()

def func(window, canvas):
    """Main UI layout for entering a new note."""
    style = ttk.Style()

    style.configure('Buttons.TButton',
                    foreground='white',
                    background='#3f3752',
                    borderwidth=2,
                    relief='raised',
                    highlightcolor='#dbd8e3',
                    bordercolor='#dbd8e3',
                    font=('Times New Roman', 13))

    style.configure('Entry.TEntry',
                    foreground='white',
                    background='#79c2d0',
                    font=('Times New Roman', 13))

    welcome = canvas.create_text(550, 100,
                                 text='Access Existing Notes',
                                 fill='white',
                                 anchor='center')

    name = ttk.Entry(window, style='Entry.TEntry')
    canvas.create_window(550, 150, anchor='center', window=name)

    guide = canvas.create_text(450, 150, text="Name", fill="white", anchor="center")

    open_button = ttk.Button(window, text='Open', command=lambda: old_note(window, canvas, name), style='Buttons.TButton')
    canvas.create_window(600, 200, anchor='center', window=open_button)

    create_button = ttk.Button(window, text='New Note', command=lambda: new_note(window, canvas, [], [], name), style='Buttons.TButton')
    canvas.create_window(550, 350, anchor='center', window=create_button)

    boanvas = Canvas(window, width=350, height=400)
    boanvas.place(x=10, y=50, width=350, height=400)

    scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=boanvas.yview)
    scrollbar.place(x=350, y=50, height=400)
    boanvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind('<Configure>', lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    file_path = "Data/List.txt"
    populate(file_path, scrollable_frame)

def welcome():
    """Main welcome window setup."""
    window = ttk.Window(themename="darkly")
    window.title("Rock Paper Scissors")
    window.geometry('700x500')
    window.resizable(False, False)

    canvas = Canvas(window, width=700, height=500)
    canvas.place(x=0, y=0, relwidth=1.5, relheight=1.5)

    func(window, canvas)

    window.mainloop()

welcome()
