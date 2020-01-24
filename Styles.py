import csv
import tkinter as tk


class Style:
    def __init__(self, name, primary, secondary, tertiary, fourth, background):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary
        self.fourth = fourth
        self.background = background

def change_style(name, primary, secondary, tertiary, fourth, background):
    settings_file = open('current_settings.csv', 'wb', newline='')
    settings_writer = csv.writer(settings_file)
    override = {1:[name, primary, secondary, tertiary, fourth, background]}



def pick_style(current_style):
    root = tk.Tk()

    HEIGHT = 100
    WIDTH = 175

    canvas2 = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas2.pack()

    frame = tk.Frame(root, bg=current_style.tertiary)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(frame, text='Enter the Week #', bg='#000000', fg='#ffffff')
    label.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

    entry = tk.Entry(frame, font=25)
    entry.place(relx=.25, rely=.4, relwidth=.2, relheight=.3)

    button = tk.Button(frame, font=25, text='Go', bg='#F9DD16')
    button.place(relx=.45, rely=.4, relwidth=.2, relheight=.3)

    root.mainloop()


themes = open('settings.csv')
themes_reader = csv.reader(themes)
themes_list = list(themes_reader)

settings = open('current_settings.csv')
settings_reader = csv.reader(settings)
settings_list = list(settings_reader)

current_style = Style(settings_list[1][0], settings_list[1][1], settings_list[1][2],
                settings_list[1][3], settings_list[1][4], settings_list[1][5])
