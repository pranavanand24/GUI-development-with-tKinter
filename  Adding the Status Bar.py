from Tkinter import *

def doNothing():
    print("ok ok I won't ...")
    
root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project", command =doNothing)
subMenu.add_command(label="New", command =doNothing)
subMenu.add_command(label="save", command =doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command =doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)


status = Label(root,text="Interface Under Construction", bd=1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()