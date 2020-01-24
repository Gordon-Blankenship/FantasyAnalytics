import tkinter as tk
from PIL import Image, ImageTk
import TeamsGraphed as tg
import Styles as style

HEIGHT = 600
WIDTH = 750
LEAGUE = 'Lambeau League'


def graph_search(entry):
    if entry == LEAGUE:
        root2 = tk.Tk()

        HEIGHT2 = 100
        WIDTH2 = 175

        canvas2 = tk.Canvas(root2, height=HEIGHT2, width=WIDTH2)
        canvas2.pack()

        frame = tk.Frame(root2, bg=style.current_style.primary)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        label2 = tk.Label(frame, text='Enter the Week #', bg=style.current_style.tertiary, fg=style.current_style.fourth)
        label2.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        entry2 = tk.Entry(frame, font=25)
        entry2.place(relx=.25, rely=.4, relwidth=.2, relheight=.3)

        button2 = tk.Button(frame, font=25, text='Go', bg='#F9DD16', command=lambda: tg.plot_teams(entry2.get()))
        button2.place(relx=.45, rely=.4, relwidth=.2, relheight=.3)

        root2.mainloop()
    elif entry == LEAGUE + ' team totals':
        tg.current_totals()

    else:
        label['font'] = 50
        label['text'] = 'No Results Found'


# everything goes into the root
root = tk.Tk()

results_box = 'Enter the graphs you would like to search above'
# canvas is a background, can have multiple canvases
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#000000')
canvas.pack()

mascot = Image.open('C:\\Users\\trebl\\PycharmProjects\\FantasyAnalytics\\images\\' + style.current_style.background)
background_image = ImageTk.PhotoImage(mascot)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# frames go in canvases, multiple frames in a canvas
top_frame = tk.Frame(root, bg=style.current_style.primary)
top_frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

# interactive typing bars
entry = tk.Entry(top_frame, bg='#a4a4a6', font=50)
entry.place(relx=.025, rely=.175, relwidth=.65, relheight=.65)

# buttons can be used whenever
button = tk.Button(top_frame, bg=style.current_style.secondary, fg=style.current_style.tertiary, text='Search Graphs', command=lambda: graph_search(entry.get()))
button.place(relx=0.7, rely=0.175, relwidth=.275, relheight=.65)

lower_frame = tk.Frame(root, bg=style.current_style.tertiary)
lower_frame.place(relx=0.5, rely=0.25, relwidth=.75, relheight=.625, anchor='n')

label = tk.Label(lower_frame, bg='#a4a4a6')
label.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

# closing the root
root.mainloop()
