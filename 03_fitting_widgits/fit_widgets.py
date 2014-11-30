try:    #python2
	from Tkinter import *
except ImportError:
	#python3
	from tkinter import *


mainwindow = Tk()

# create layouts
toplayout = Frame(master=mainwindow, height=100, width=400)
middlelayout = Frame(mainwindow)
bottomlayout = Frame(mainwindow)

# layout options are pack, grid, and place
toplayout.pack()
middlelayout.pack()
bottomlayout.pack()

# createn widgets
label01 = Label(toplayout, text='Button 1', bg='red', fg='white')
label02 = Label(middlelayout, text='Button 2', bg='blue', fg='white')
label03 = Label(bottomlayout, text='Button 3', bg='green', fg='white')

# add widgets to layout using pack, place, or grid
# read more: http://www.python-course.eu/tkinter_layout_management.php
# NEVER MIX pack, place, and grid in the same frame
#pack

label01.pack(side=LEFT, fill=NONE)
label02.pack(side=LEFT, fill=NONE)
label03.pack(side=RIGHT,fill=NONE)

#place, read more http://effbot.org/tkinterbook/place.htm
'''
label01.place(x=0, y=0, anchor=NW)
label02.place(x=5, y=5, anchor=CENTER)
label03.place(x=10, y=10, anchor=SE)
'''
#grid, read me http://effbot.org/tkinterbook/grid.htm
'''
label01.grid(row=0, column=0)
label02.grid(row=1, column=1)
label03.grid(row=2, column=2)

'''


mainwindow.mainloop()
###end###
