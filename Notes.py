import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Text, Entry, messagebox
from ttkbootstrap.constants import *
import tkinter as tk

def delete_bist(bist, canvas):

    for i in bist:
        canvas.delete(i)

def delete_cist(cist):
   
    for i in cist:
        i.destroy()

def populate_data(file_path, frame, state):

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
    
    with open(file_path, 'r') as file:
        data = file.read() 

    paragraphs = data.split("\n\n")  # Split the content into paragraphs using double newlines

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

def save_note(file_path, frame):
    
    all_text = []
    for widget in frame.winfo_children():
        if isinstance(widget, Text):
            content = widget.get("1.0", tk.END).strip()
            all_text.append(content + "\n")  # Add the content of the Text widget to the list

    with open(file_path, 'w') as file:
        file.writelines(all_text)  # Save all content back to the file

def new_note(window, canvas):

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

    Note = ttk.Window(themename="darkly")
    Note.title("Name")
    Note.geometry("400x300")
    Note.resizable(False, False)

    boanvas = Canvas(Note, 
                     width=400, 
                     height=300)
    boanvas.place(x=0, 
                  y=0, 
                  width=400, 
                  height=300)

    name = ttk.Entry(Note,
                     style = "Entry.TEntry")
    boanvas.create_window(200,150,
                         anchor='center',
                         window=name)

    names = boanvas.create_text(100,150,
                                text='name',
                                fille='white',
                                anchor='center')


def old_note(window, canvas, name):
    
    note_name = name.get()

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

    try:
        with open("List.txt", "a") as file:
            file.write(note_name + "\n")

    except Exception as e:
        print("Error at line 11 : ", e)

    Note = ttk.Window(themename="darkly")
    Note.title(note_name)
    Note.geometry("400x300")
    Note.resizable(False, False)

    boanvas = Canvas(Note, 
                     width=400, 
                     height=300)
    boanvas.place(x=0, 
                  y=0, 
                  width=400, 
                  height=300)

    scrollbar = ttk.Scrollbar(Note, 
                              orient=VERTICAL, 
                              command=boanvas.yview)
    scrollbar.place(x=380, 
                    y=0, 
                    height=300)
    boanvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0),
                           window=scrollable_frame, 
                           anchor="nw")

    scrollable_frame.bind('<Configure>',
                          lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    # Populate the scrollable frame with editable text widgets from the file
    file_path = "Data/" + note_name + ".txt"
    state = "normal"
    populate_data(file_path, scrollable_frame, state)

    # Save button to save edited note
    save_button = ttk.Button(Note, 
                             text="Save", 
                             command=lambda: save_note(file_path, scrollable_frame))
    save_button.place(x=170, 
                      y=270)

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

    welcome = canvas.create_text(450, 100,
                                 text='Access Existing Notes',
                                 fill='white',
                                 anchor='center')

    name = ttk.Entry(window, 
                     style='Entry.TEntry')
    canvas.create_window(450, 150,
                         anchor='center',
                         window=name)

    guide = canvas.create_text(350, 150, 
                               text="Name", 
                               fill="white", 
                               anchor="center")

    open_button = ttk.Button(window, 
                             text='Open', 
                             command=lambda: old_note(window, canvas, name), 
                             style='Buttons.TButton')
    canvas.create_window(500, 200, 
                         anchor='center', 
                         window=open_button)

    create_button = ttk.Button(window, 
                               text='New Note', 
                               command=lambda: new_note(window, canvas), 
                               style='Buttons.TButton')
    canvas.create_window(450, 350, 
                         anchor='center', 
                         window=create_button)

    boanvas = Canvas(window, 
                     width=200, 
                     height=400)
    boanvas.place(x=10, y=50, 
                  width=200, 
                  height=400)

    scrollbar = ttk.Scrollbar(window, 
                              orient=VERTICAL, 
                              command=boanvas.yview)
    scrollbar.place(x=200, 
                    y=50, 
                    height=400)
    boanvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(boanvas)
    boanvas.create_window((0, 0), 
                          window=scrollable_frame, 
                          anchor="nw")

    scrollable_frame.bind('<Configure>', 
                          lambda e: boanvas.configure(scrollregion=boanvas.bbox('all')))

    file_path = "Data/List.txt"
    state = "disabled"
    populate_data(file_path, scrollable_frame, state)

def welcome():
    """Main welcome window setup."""
    window = ttk.Window(themename="darkly")
    window.title("Note")
    window.geometry('700x500')
    window.resizable(False,False)

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
