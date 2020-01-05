from Tkinter import *

def doNothing():
    print("ok ok I won't ...")
    
    

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
editMenu.add_command(label="Redo",command=doNot
                     

                     
toolbar=Frame (root, bg="red")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=y)

printButt = Button(toolbar, text="print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=y)

toolbar.pack(side=TOP, fill=X)

root = Tk()                
                
root.mainloop()



    