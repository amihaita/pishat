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

#topframe = Frame(mainwindow, padx=10, pady=10)
#topframe.pack(side=LEFT)

label_name = Label(mainwindow, text='Name: ')
label_name.grid(row=0, column=0)
label_email = Label(mainwindow, text='Email: ')
label_email.grid(row=1, column=0)

entry_name = Entry(mainwindow)
entry_name.grid(row=0, column=1)
entry_email = Entry(mainwindow)
entry_email.grid(row=1, column=1)

#separator1 = Frame(topframe, height=2, bd=1, relief=SUNKEN)
#separator1.grid(row=3, columnspan=2, padx=5, pady=5)

text_output = Text(mainwindow)
text_output.config(height=1, width=30)
text_output.grid(row=4, column=0, columnspan=2)

#separator2 = Frame(mainwindow, height=2, bd=1, relief=SUNKEN)
#separator2.pack() #fill=X, padx=5, pady=5)
#separator1 = Frame(topframe, height=2, bd=1, relief=SUNKEN)
#separator1.grid(row=5, columnspan=2, padx=5, pady=5)

#bottomframe = Frame(mainwindow)
#bottomframe.pack(side=RIGHT)
button_submit = Button(mainwindow, text="Enter", bg="#fcfcf0")
button_submit.config(relief=RIDGE, bd=1)
button_submit.grid(row=6, column=0)
button_quit = Button(mainwindow, text="Quit", bg="#fcfcf0", command = quitapp)
button_quit.config(relief=RIDGE, bd=1)
button_quit.grid(row=6, column=1, sticky=E)
mainwindow.iconbitmap('floppy.ico')
mainwindow.title("My App")
mainwindow.mainloop()
###END###
