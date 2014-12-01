try:	#python2
	from Tkinter import *
except ImportError:
	#python3
	from tkinter import *

#################################################
def quitapp():
	mainwindow.destroy()
#################################################
mainwindow = Tk()

topframe = Frame(mainwindow)
topframe.pack(side=LEFT)

label_name = Label(topframe, text='Name: ')
label_name.grid(row=0, column=0)
label_email = Label(topframe, text='Email: ')
label_email.grid(row=1, column=0)

entry_name = Entry(topframe)
entry_name.grid(row=0, column=1)
entry_email = Entry(topframe)
entry_email.grid(row=1, column=1)

#separator1 = Frame(topframe, height=2, bd=1, relief=SUNKEN)
#separator1.pack(fill=X, padx=5, pady=5)

text_output = Text(topframe)
text_output.config(height=5, width=30)
text_output.grid(row=2, column=0, columnspan=2)

#separator2 = Frame(mainwindow, height=2, bd=1, relief=SUNKEN)
#separator2.pack(fill=X, padx=5, pady=5)

#bottomframe = Frame(mainwindow)
#bottomframe.pack(side=RIGHT)
button_submit = Button(topframe, text="Enter")
button_submit.grid(row=3, column=0)
button_quit = Button(topframe, text="Quit", command = quitapp)
button_quit.grid(row=3, column=1, sticky=E)

mainwindow.title("My App")
mainwindow.mainloop()
###END###
