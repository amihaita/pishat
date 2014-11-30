try:
	# python2
	from Tkinter import *
except ImportError:
	# python3
	from tkinter import *
#################################################
mw = Tk()

top_frame = Frame(mw)
top_frame.pack()
top_label = Label(top_frame, text="this is the top_frame")
top_label.pack()
button1 = Button(top_frame, text="button 1", fg="blue")
button1.pack(side="left")
button2 = Button(top_frame, text="button 2", fg="red")
button2.pack(side='left')
button3 = Button(top_frame, text="button 3", fg="green")
button3.pack(side="left")


bottom_frame = Frame(mw)
bottom_frame.pack(side=BOTTOM)
btm_label = Label(bottom_frame, text="this is the bottom_frame")
btm_label.pack()
button4 = Button(bottom_frame, text="button 4", fg="orange")
button4.pack()


mw.mainloop()
##################
#	END
#i#################
