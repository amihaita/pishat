#!/usr/bin/python

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


root = Tk() 		# create the main window
a_label = Label(root, text="tight son, ya me")
a_label.pack()		# pack the label into the main window
root.mainloop()		# paint gui on screen


#END
