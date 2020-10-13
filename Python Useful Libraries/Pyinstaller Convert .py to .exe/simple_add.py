# check this code first.
from tkinter import *

app = Tk()
# The title of the project
app.title("The title of the project")
# The size of the window
app.geometry("400x400")

# Defining a funtion
def c():
    # Label
    m = Label(app, text="Text")
    m.pack()


# Button
l = Button(app, text="The text of the Butoon", command=c)
# Packing the Button
l.pack()
app.mainloop()
# Quick Note : 
# When you put a command you should not use parentheses
# l = Button(app, text="The text of the Butoon", command=c)
# l = Button(app, text="The text of the Butoon", command=c())


