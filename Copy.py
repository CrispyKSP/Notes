import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Label, Entry
import tkinter as tk

def delete_bist():
    pass

def delete_cist():
    pass

def list(window, canvas):
    """Function to read from List.txt and display it."""
    try:
        with open("List.txt", "r") as file:
            data = file.readlines()

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        for i, line in enumerate(data):
            label = ttk.Label(frame, text=line.strip(), padding=5)
            label.grid(row=i, column=0, sticky="w")

        # Update canvas scrollregion after populating data
        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    except FileNotFoundError:
        print("File not found!")

def new_user(window, bist, name):
    """Function to create a new user entry and display in scrollable text widget."""
    root = tk.Toplevel(window)  # Use Toplevel instead of Tk to avoid second mainloop
    root.geometry('400x300')

    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    text_widget = tk.Text(frame, wrap='word', height=10, width=40)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Insert new user's note name into text_widget
    text_widget.insert(tk.END, f"New Note: {name.get()}\n")
    text_widget.config(padx=10, pady=10)

    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    root.mainloop()

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
                    foreground='black',
                    background='#79c2d0',
                    font=('Times New Roman', 13))

    # Welcome message
    welcome = canvas.create_text(350, 100,
                                 text='Good to have you',
                                 fill='white',
                                 anchor='center')

    # Ask for new note name
    ask_name = canvas.create_text(300, 150,
                                  text='Enter the name you wanna give to this new note',
                                  fill='white',
                                  anchor='center')

    # Name label and entry field
    names = canvas.create_text(250, 200,
                               text='Name',
                               fill="white",
                               anchor='center')

    name = ttk.Entry(window, style='Entry.TEntry')
    canvas.create_window(350, 200,
                         anchor='center',
                         window=name)

    # Button to enter new note
    enter_button = ttk.Button(window,
                              text='Done',
                              command=lambda: new_user(window, bist, name),
                              style='Buttons.TButton')
    canvas.create_window(350, 300,
                         anchor='center',
                         window=enter_button)

    # Button to go back
    back_button = ttk.Button(window,
                             text='Back',
                             command=lambda: func(window),
                             style='Buttons.TButton')
    canvas.create_window(350, 350,
                         anchor='center',
                         window=back_button)

    # Store elements for deletion if needed
    bist = [welcome, ask_name, names]
    cist = [name, enter_button, back_button]

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
