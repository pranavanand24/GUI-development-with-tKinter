from Tkinter import *

root  = Tk()

canvas = Canvas(root, width=100, height=200)
canvas.pack()

blackLine = canvas.create_line(0,0,200,55)
redline =  canvas.create_line(0,100,200,50, fill="red")
greenline = canvas.create_rectangle(25,35,130,60, fill="green")

root.mainloop()

