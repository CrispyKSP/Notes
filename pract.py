import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Text, Entry, messagebox, Toplevel, VERTICAL
from ttkbootstrap.constants import *
import tkinter as tk
import os

def populate_list_slowly(frame, file_list, delay=500):
    """Populate list of files one by one with a delay between each item."""

    for i, file_name in enumerate(file_list):
        frame.after(i * delay, lambda file_name=file_name: add_textbox(frame, file_name))

def add_textbox(frame, file_name):
    """Add a text widget displaying a file name."""
    text_box = ttk.Label(frame, text=file_name, style='Label.TLabel')
    text_box.pack(anchor='w', padx=5, pady=5)

def show_file_list_slowly(window, file_path, cist):
    """Simulate slow file loading effect when the button is pressed."""

    delete_window(cist)

    boanvas = Canvas(window, 
                     width=200, 
                     height=400)
    boanvas.place(x=10, y=50, 
                  width=200, 
                  height=400)

    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), 
                          window=scrollable_frame, 
                          anchor="nw")

    scrollbar = ttk.Scrollbar(window, 
                              orient=VERTICAL, 
                              command=boanvas.yview)
    scrollbar.place(x=200, 
                    y=50, 
                    height=400)
    boanvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame.bind('<Configure>', 
                          lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    try:
        with open(file_path, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        data = ""  # Handle file not found for simplicity

    file_list = data.split("\n")  # Assuming each line contains a file name
    delay_per_file = 100  # Delay per file in milliseconds (e.g., 100ms per file)
    total_time = 5000  # Total time for the whole list to appear (5 seconds)
    
    file_count = len(file_list)
    if file_count > 0:
        delay_per_file = total_time // file_count  # Adjust delay based on file count

    populate_list_slowly(scrollable_frame, file_list, delay=delay_per_file)

def delete_canvas(bist, canvas):

    for i in bist:
        canvas.delete(i)

def delete_window(cist):
   
    for i in cist:
        i.destroy()

def populate_data(file_path, frame, state):

    try:
        with open(file_path, 'r') as file:
            data = file.read() 

        paragraphs = data.split("\n\n")  # Split the content into paragraphs using double newlines
    except FileNotFoundError:
        pass

    for i, paragraph in enumerate(paragraphs):
        
        text_box = Text(frame, 
                        wrap="word",
                        height=100, 
                        width=60)  # Larger height for paragraphs
        text_box.insert("1.0", 
                        paragraph.strip())  # Insert the paragraph into the Text widget
        text_box.grid(row=i, 
                      column=0, 
                      sticky="w", 
                      padx=5, 
                      pady=5)  # Place the Text widget with padding

        # Optional: Disable Text widget initially to prevent editing, can be enabled on demand
        text_box.config(state=state)  # Or set to "disabled" if you want read-only initially

def create_file(file):

    name = file.get()

    with open("Data/List.txt","a") as f:
        f.write(name+"\n")

    new = "Data/"+name+".txt"
    with open(new,"w") as f:
        pass

    old_note(new,file,2)
    
def save_note(file_path, frame):
    
    all_text = []
    for widget in frame.winfo_children():
        if isinstance(widget, Text):
            content = widget.get("1.0", tk.END).strip()
            all_text.append(content + "\n")  # Add the content of the Text widget to the list

    with open(file_path, 'w') as file:
        file.writelines(all_text)  # Save all content back to the file

def old_note(name,file,num):

    # Configure style for buttons and entry
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

    note_name = name[5:-4]

    with open("Data/List.txt","r")as f:
        lists = f.read()
        names = lists.split('\n')

    if note_name in names or num == 2:
        # Creating a new window using ttkbootstrap's theming system
        Note = Toplevel()
        Note.title(note_name)
        Note.geometry("400x300")
        Note.resizable(False, False)

        canvas = Canvas(Note, 
                        width=400, 
                        height=300)
        canvas.place(x=0, 
                     y=0, 
                     width=400, 
                     height=300)

        scrollbar = ttk.Scrollbar(Note, 
                                  orient=VERTICAL, 
                                  command=canvas.yview)

        scrollbar.place(x=380, 
                        y=0, 
                        height=300)

        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0),
                              window=scrollable_frame, 
                              anchor="nw")

        scrollable_frame.bind('<Configure>', 
                              lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Populate the scrollable frame with editable text widgets from the file
        file_path = "Data/"+note_name +".txt"
        state = "normal"
        populate_data(file_path, scrollable_frame, state)   
        # Save button to save edited note
        save_button = ttk.Button(Note, 
                                 text="Save", 
                                 style="Buttons.TButton", 
                                 command=lambda: save_note(file_path, scrollable_frame))
        save_button.place(x=170, y=270)

        Note.mainloop()

    else :
        file.delete(0, END)
        # Insert new data into the Entry widget
        file.insert(0, "Not Found")

def NEW_Note(window, canvas, button, i):

    button.destroy()

    a=0

    if i == 2:
        a = 120

    name = canvas.create_text(250+a, 350,
                              text='New Name',
                              fill='white',
                              anchor='center')

    enter = ttk.Entry(window, 
                      style='Entry.TEntry')
    canvas.create_window(350+a, 350,
                         anchor='center',
                         window=enter)

    proceed = ttk.Button(window, 
                         text='Create', 
                         command=lambda: create_file(enter), 
                         style='Buttons.TButton')
    canvas.create_window(400+a, 400, 
                         anchor='center', 
                         window=proceed)

def animate_text(window, canvas, i=0):
    """Animates the text and entry field horizontally."""
    
    if i >= 120:
        return  # Stop the animation when it reaches 450 pixels

    # Clear previous widgets
    canvas.delete("all")

    welcome = canvas.create_text(350+i, 100,
                                     text='Access Existing Notes',
                                     fill='white',
                                     anchor='center')

    name = ttk.Entry(window, 
                         style='Entry.TEntry')
    canvas.create_window(350+i, 150,
                             anchor='center',
                             window=name)

    guide = canvas.create_text(250+i, 150, 
                                   text="Name", 
                                   fill="white", 
                                   anchor="center")

    pen_button = ttk.Button(window, 
                                 text='Open', 
                                 command=lambda:  get_name(name), 
                                 style='Buttons.TButton')
    canvas.create_window(400+i, 200, 
                             anchor='center', 
                             window=pen_button)

    open_button = ttk.Button(window, 
                                 text='Show List', 
                                 style='Buttons.TButton',
                                 command=lambda: show_file_list_slowly(window, 'Data/List.txt', cist))
    canvas.create_window(300+i, 
                             200, 
                             anchor='center', 
                             window=open_button)

    create_button = ttk.Button(window, 
                                   text='New Note', 
                                   command=lambda: NEW_Note(window, canvas, create_button,2),
                                   style='Buttons.TButton')
    canvas.create_window(350+i, 350, 
                             anchor='center', 
                             window=create_button)

    cist = []
    # Continue the animation by scheduling the next frame
    window.after(5, animate_text, window, canvas, i + 1)

def get_name(name):
    namer = name.get()
    if namer == "":
        name.delete(0, END)
        # Insert new data into the Entry widget
        name.insert(0, "Not Found")

    else:
        names = "Data/"+namer+".txt"
        old_note(names,name,1)

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

    welcome = canvas.create_text(350, 100,
                                     text='Access Existing Notes',
                                     fill='white',
                                     anchor='center')

    name = ttk.Entry(window, 
                         style='Entry.TEntry')
    canvas.create_window(350, 150,
                             anchor='center',
                             window=name)

    guide = canvas.create_text(250, 150, 
                                   text="Name", 
                                   fill="white", 
                                   anchor="center")

    pen_button = ttk.Button(window, 
                                 text='Open', 
                                 command=lambda: get_name(name), 
                                 style='Buttons.TButton')
    canvas.create_window(400, 200, 
                             anchor='center', 
                             window=pen_button)

    open_button = ttk.Button(window, 
                             text='Show List', 
                             style='Buttons.TButton',
                             command=lambda: 
                             (animate_text(window, canvas), 
                             show_file_list_slowly(window, 'Data/List.txt', cist)))
    canvas.create_window(300, 
                         200, 
                         anchor='center', 
                         window=open_button)

    create_button = ttk.Button(window, 
                                   text='New Note', 
                                   command=lambda: NEW_Note(window, canvas, create_button, 1), 
                                   style='Buttons.TButton')
    canvas.create_window(350, 350, 
                             anchor='center', 
                             window=create_button)

    cist = []
            
def welcome():
    """Main welcome window setup."""
    window = ttk.Window(themename="darkly")
    window.title("Note")
    window.geometry('700x500')
    window.resizable(False, False)

    canvas = Canvas(window, 
                    width=700, 
                    height=500)
    canvas.place(x=0, 
                 y=0, 
                 relwidth=1.5, 
                 relheight=1.5)

    func(window, canvas)

    window.mainloop()

welcome()
