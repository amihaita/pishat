from Tkinter import *

#################################################

def copytext():
	#print entry_1.get()
	entry_2.delete(0, END)  #remove any previous contents
	entry_2.insert(0, entry_1.get())
#################################################

mw = Tk()

label_1 = Label(mw, text="Enter some text: ")
entry_1 = Entry(mw)
label_2 = Label(mw, text='Output: ')
entry_2 = Entry(mw)
button_1 = Button(mw, text="Submit", command=copytext)

label_1.grid(row=0, column=0, sticky=W)
entry_1.grid(row=0, column=1)
label_2.grid(row=1, column=0, sticky=W)
entry_2.grid(row=1, column=1)
button_1.grid(row=3, columnspan=2, sticky=E)


mainloop()
