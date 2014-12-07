from Tkinter import *
#################################################

class MainWindow:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack(padx=10, pady=10)

		self.label_1 = Label(frame, text="User Name: ")
		self.entry_1 = Entry(frame)
		self.label_2 = Label(frame, text="Password: ")
		self.entry_2 = Entry(frame)

		self.label_1.grid(row=0, column=0, sticky=E)
		self.entry_1.grid(row=0, column=1)
		self.label_2.grid(row=1, column=0, sticky=E)
		self.entry_2.grid(row=1, column=1)

		self.button_1 = Button(frame, text="Submit", command=self.get_input)
		self.button_2 = Button(frame, text="Quit", command=self.quitapp)
		self.button_1.grid(row=2, column=0)
		self.button_2.grid(row=2, column=1)	

	def get_input(self):
		print("Submit button pressed")

	def quitapp(self):
		frame.quit()
		
				

mw = Tk()
app = MainWindow(mw)
mainloop()
