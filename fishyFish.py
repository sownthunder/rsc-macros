"""
Created 9/06/2017
- 15 years after the creation of Slegger...

FishyFish.py

"So Long and Thanks for All the Fish"

"""

# import the goodies
import pyautogui
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# get/set screen resolution
width, height = pyautogui.size()

# get/set the coordinates of the mouse
# <variableName> pyautogui.position()

#pyautogui.moveTo(x = None, y = None, duration = 0.0, .,.etc)
# ^^ MOVES THE MOUSE CURSOR TO A POINT ON THE SCREEN ^^

# MAGICALLY MOVE MOUSE TO 10 x coord and 10 y coord on screen
# pyautogui.moveTo(10, 10)

def testFish():
    # move mouse to position that takes 2 seconds?
    pyautogui.moveTo(10, 10, duration=2)
    pyautogui.moveRel(200,0, duration = 1)
    pyautogui.moveRel(0, 200, duration=1)
    # pyautogui.doubleClick(339, 38)
    # click into notepad (applicaiton is already waiting there)
    ## print ("mouse pos == " + str(pyautogui.displayMousePosition())) <-- 9/12/2017 removed because function is cmd line only
    # X: 2580 Y:  601 (9/12/2017)\
    pyautogui.click(210, 210)
    # type test message
    pyautogui.typewrite('Hello world!"')
    pyautogui.click
    return

def alphaRun():
    # take screen shot and save to C drive
    pyautogui.screenshot('c:\\temp\\screenshot_example.png')
    x = 2
    return

app = tk.Tk()
app.title('FishyFish.exe')
app.geometry('400x400+200+200')

buttonBeginFish = tk.Button(app, text="So Long and Thanks for All the Fish", width=50, command=testFish)
buttonBeginFish.pack()

buttonAlphaRun = tk.Button(app, text="Alpha RUN", width =20, command=alphaRun)
buttonAlphaRun.pack()

app.config()
app.mainloop()
