import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Label, Entry, messagebox
from ttkbootstrap.constants import *
import tkinter as tk

def delete_bist(bist,canvas):

    for i in bist:
        canvas.delete(i)

def delete_cist(cist):

    for i in cist:
        i.destroy()

def populate_data(file_path, frame):
    """Read data from the file and add it to the scrollable frame."""
    with open(file_path, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        label = ttk.Label(frame, text=line.strip(), padding=2)
        label.grid(row=i, column=0, sticky="w")

def old_note(window, canvas, name):

    note_name = name.get()

    try:
        with open("List.txt","a") as file:
            file.write(note_name)

    except Exception as e:
        print("Error at line 11 : ", e)

    Note = ttk.Window(themename = "darkly")
    Note.title(note_name)
    Note.geometry("200x200")
    Note.resizable(False,False)

    boanvas = Canvas(Note,
                     width=200,  # Set an appropriate width
                     height=200)  # Make it taller to allow scrolling
    boanvas.place(x=0,
                  y=0,  # Adjust y position to fit within the main canvas
                  width=200,
                  height=200)

    # Create a scrollbar and link it to the boanvas
    scrollbar = ttk.Scrollbar(Note, orient=VERTICAL, command=boanvas.yview)
    scrollbar.place(x=180, y=0, height=200)  # Place the scrollbar next to the boanvas

    boanvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the boanvas
    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Bind configuration events to dynamically adjust the scroll region
    scrollable_frame.bind('<Configure>', lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    # Populate the scrollable frame with data from a file
    file_path = "Data/"+note_name+".txt"
    populate_data(file_path, scrollable_frame)

    Note.mainloop()

    try:
        with open(open_note, "w") as file:
            data = file.writelines()

    except Exception as e:
        print("Error at line 24 :", e)

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

    name = ttk.Entry(window, 
                     style='Entry.TEntry')
    canvas.create_window(550, 150,
                         anchor='center',
                         window=name)

    guide = canvas.create_text(450, 150,
                               text="Name",
                               fill="white",
                               anchor="center")

    open_button = ttk.Button(window,
                        text='Open',
                        command=lambda: old_note(window,canvas, name),
                        style='Buttons.TButton')
    canvas.create_window(600, 200,
                         anchor='center',
                         window=open_button)

    create_button = ttk.Button(window,
                        text='New Note',
                        command=lambda: new_note(window,canvas, bist, cist, name),
                        style='Buttons.TButton')
    canvas.create_window(550, 350,
                         anchor='center',
                         window=create_button)

    boanvas = Canvas(window,
                     width=350,  # Set an appropriate width
                     height=400)  # Make it taller to allow scrolling
    boanvas.place(x=10,
                  y=50,  # Adjust y position to fit within the main canvas
                  width=350,
                  height=400)

    # Create a scrollbar and link it to the boanvas
    scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=boanvas.yview)
    scrollbar.place(x=150, y=50, height=400)  # Place the scrollbar next to the boanvas

    boanvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the boanvas
    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Bind configuration events to dynamically adjust the scroll region
    scrollable_frame.bind('<Configure>', lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    # Populate the scrollable frame with data from a file
    file_path = "Data/List.txt" 
    populate_data(file_path, scrollable_frame)


    bist = []
    cist = []



def welcome():
    """Main welcome window setup."""
    window = ttk.Window(themename="darkly")
    window.title("Rock Paper Scissors")
    window.geometry('700x500')
    window.resizable(False, False)

    # Main canvas for the application
    canvas = Canvas(window,
                    width=700,
                    height=500)
    canvas.place(x=0,
                 y=0,
                 relwidth=1.5,
                 relheight=1.5)

    # Initialize main UI function
    func(window, canvas)

    window.mainloop()

welcome()
