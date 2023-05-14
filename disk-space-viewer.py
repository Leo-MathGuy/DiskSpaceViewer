# Do imports
from tkinter import *

# Root size
root = Tk()
root.title("Disk Space")
root.geometry("500x550")

# Canvas element
c = Canvas(root, width=500, height=500)
c.place(x=0, y=0, width=500, height=500)

# Stop the window
def stop():
    global run
    run = False

# The quit button
quit_button = Button(
    root,
    width=102,
    height=52,
    command=stop, # Stop
    text="Quit",
    background="red",
    foreground="white",
    activebackground="#DD6666", # Hover background
    activeforeground="white"    # Hover text color
)
quit_button.place(x=400, y=500, width=102, height=52) # Place in bottom-right

# The percent text
percent_text = Label(
    root,
    width=400,
    height=50,
    text="Loading...",
    fg="Black",
    font="Roboto 15", # 15px Roboto
    justify="left",
)
percent_text.place(x=0, y=500, width=400, height=50)

# Seperator between canvas and text
seperator = Frame(
    root,
    height=2,
    width=500,
    background="black"
)
seperator.place(x=0, y=500, width=500, height=2)

# Squares
squares = []
for i in range(0, 100): # X pos
    squares.append(list())
    for j in range(0, 100): # Y pos
        squares[-1].append(c.create_rectangle(i*5, j*5, i*5+5, j*5+5, fill="grey"))

# Percent to color
def percent_to_color(percent: float) -> str: #  Thanks to a random guy on stackoverflow for this
    def rgb_to_hex(rgb): # Thanks to another random guy on stackoverflow for this
        return "#%02x%02x%02x" % rgb
    pct_diff = 1.0 - percent
    red_color = min(255, pct_diff * 2 * 255)
    green_color = min(255, percent * 2 * 255)
    colors = (round(red_color), round(green_color), 0)
    return rgb_to_hex(colors)

percent = 0
run = True
while run:
    # Read file
    try:
        with open("/var/diskpercent.txt", "r") as f:
            percent = f.read().split("\n")[0]
            if percent != '':
                try: # Sometimes line is empty, but is not detected by == '' for some reason
                    # Update text
                    percent_text.configure(percent_text, text=str(float(percent))+"% Free")
                except:
                    pass
    except:
        pass
    
    # Try to update percent
    try:
        percent = float(percent)
    except:
        continue
        
    # 10000 Squares
    for i in range(0, 100):
        for j in range(0, 100):
            if percent > 0.0001:
                c.itemconfig(squares[i][j], fill="#00FF00") # Yes
            elif percent <= 0:
                c.itemconfig(squares[i][j], fill="#FF0000") # No
            else:
                c.itemconfig(squares[i][j], fill=percent_to_color(percent*10000)) # Maybe
            percent -= 0.0001
                
    root.update()
