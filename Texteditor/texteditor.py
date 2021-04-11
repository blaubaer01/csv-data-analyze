import tkinter.filedialog
from tkinter import *

class App:

    def doNew(self):
            # Clear the text
            self.text.delete(0.0, END)

    def doSaveAs(self):
            # Returns the saved file
            file = tkinter.filedialog.asksaveasfile(mode='w')
            textoutput = self.text.get(0.0, END) # Gets all the text in the field
            file.write(textoutput.rstrip()) # With blank perameters, this cuts off all whitespace after a line.
            file.write("\n") # Then we add a newline character.

    def doOpen(self):
            # Returns the opened file
            file = tkinter.filedialog.askopenfile(mode='r')
            fileContents = file.read() # Get all the text from file.

            # Set current text to file contents
            self.text.delete(0.0, END)
            self.text.insert(0.0, fileContents)

    def __init__(self):
            # Set up the screen, the title, and the size.
            self.root = Tk()
            self.root.title("Basic Notepad")
            self.root.minsize(width=1000,height=500)

            # Set up basic Menu
            menubar = Menu(self.root)

            # Set up a separate menu that is a child of the main menu
            filemenu = Menu(menubar,tearoff=0)
            filemenu.add_command(label="New File", command=self.doNew, accelerator="Ctrl+N")

            # Try out openDialog
            filemenu.add_command(label="Open", command=self.doOpen, accelerator="Ctrl+O")

            # Try out the saveAsDialog
            filemenu.add_command(label="Save", command=self.doSaveAs, accelerator="Ctrl+Shift+S")
            menubar.add_cascade(label="File", menu=filemenu)
            self.root.config(menu=menubar)

            # Set up the text widget
            self.text = Text(self.root)
            self.text.pack(expand=YES, fill=BOTH) # Expand to fit vertically and horizontally

app = App()
app.root.mainloop()
