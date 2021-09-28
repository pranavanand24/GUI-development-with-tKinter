# Python-GUI-with-tKinter

Getting started with Python tkinter GUI

Python offers multiple options for developing GUI (Graphical User Interface).
Out of all the GUI methods, tkinter is most commonly used method. 
It is a standard Python interface to the Tk GUI toolkit shipped with Python. 
Python with tkinter outputs the fastest and easiest way to create the GUI applications. 
Creating a GUI using tkinter is an easy task.
To create a tkinter:

Importing the module – tkinter
Create the main window (container)
Add any number of widgets to the main window
Apply the event Trigger on the widgets.

Importing tkinter is same as importing any other module in the python code.
Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x is ‘tkinter’.

import tkinter
There are two main methods used you the user need to remember while creating the Python application with GUI.
To create a main window, tkinter offers a method 

Tk (screenName=None,  baseName=None,  className=’Tk’,  useTk=1) 
To change the name of the window, you can change the className to the desired one. 
The basic code used to create the main window of the application is:
m=tkinter.Tk() where m is the name of the main window object

mainloop():There is a method known by the name mainloop() is used when you are ready for the application to run. 
mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
m.mainloop()
