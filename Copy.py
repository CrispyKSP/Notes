import ttkbootstrap as ttk
from tkinter import Canvas, Scrollbar, Label, Entry
import tkinter as tk

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

    name = ttk.Entry(window, style='Entry.TEntry')
    canvas.create_window(350+i, 150, anchor='center', window=name)

    pen_button = ttk.Button(window, text='Open',
                            command=lambda: func(window, canvas),
                            style='Buttons.TButton')
    canvas.create_window(350+i, 200, anchor='center', window=pen_button)

    # Continue the animation by scheduling the next frame
    window.after(5, animate_text, window, canvas, i + 1)

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

    # Create initial UI elements
    welcome = canvas.create_text(350, 100,
                                 text='Access Existing Notes',
                                 fill='white',
                                 anchor='center')

    name = ttk.Entry(window, style='Entry.TEntry')
    canvas.create_window(350, 150, anchor='center', window=name)

    pen_button = ttk.Button(window, text='Open',
                            command=lambda: animate_text(window, canvas),
                            style='Buttons.TButton')
    canvas.create_window(350, 200, anchor='center', window=pen_button)       

def welcome():
    """Main welcome window setup."""
    window = ttk.Window(themename="darkly")
    window.title("Note")
    window.geometry('700x500')
    window.resizable(False, False)

    canvas = Canvas(window, width=700, height=500)
    canvas.place(x=0, y=0, relwidth=1.5, relheight=1.5)

    cist = bist = variable = 0

    func(window, canvas)

    window.mainloop()

welcome()
