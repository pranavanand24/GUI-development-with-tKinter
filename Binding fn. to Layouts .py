from Tkinter import *
root = Tk()

def printName():
    print("My name is Pranav Anand")
    
button_1 = Button(root, text="Print my name", command=printName)
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()