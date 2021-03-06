"""
Created 9/06/2017
- 15 years after the creation of Slegger...

FishyFish.py

"So Long and Thanks for All the Fish"

"""

# import the goodies
import glob # to get list of file names as images for screenshots to know wher to click
import time
import pyautogui
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

global start, end

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
    # start timer?
    start = time.time()
    print ('hello')
    end = time.time()
    print (end - start)
    # take screen shot and save to C drive
    pyautogui.screenshot('c:\\temp\\screenshot_example.png')
    # where (location) the program can find our scrreenshot image
    #pyautogui.locateOnScreen(r'c:\temp\outbound\calc7key.png')
    ### <--- DO LOOPS AND CHECK UNTIL THAT PICTURE "is found"
    print (str(pyautogui.locateOnScreen(r'c:\temp\fish2.png')))
    # attempt to right click screen and look for fishing spot
    pyautogui.alert('you have 2.5 seconds to move mouse to fishing position')
    pyautogui.PAUSE = 2.5
    pyautogui.click(button='right')
    pyautogui.moveRel(10, 0, duration=1)
    # AUTO CLICK FOR 20 NOW BUT SET TO DEPEND ON USER INPUT
    pyautogui.click(clicks=80, interval=2, button='left')
    # take screenie of "fishing spot"?
    #pyautogui.screenshot('c:\\temp\\rightClickFish.png')
    return

def importImageSelection():

    app.imageSelect = filedialog.askopenfilename(initialdir = "C:\"", title="import IMAGE select", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg"), ("all files", "*.*")))
    imageSelectLocation = str(app.imageSelect)
    # set variable above to tk.string
    imageSelectLocationText.set(imageSelectLocation)
    # take from tk.string and set it to search for that screenshot
    print (str(pyautogui.locateOnScreen(imageSelectLocationText.get())))
    return

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)


app = tk.Tk()
app.title('FishyFish.exe')
app.geometry('400x400+200+200')

buttonBeginFish = tk.Button(app, text="So Long and Thanks for All the Fish", width=50, command=testFish)
buttonBeginFish.pack()

## INCLUDE BUTTON FOR 'AUTO' AND 'MANUAL' FOR FISHING SPOTS
buttonAlphaRun = tk.Button(app, text="Alpha RUN", width =20, command=alphaRun)
buttonAlphaRun.pack()

labelClickNumberText = tk.StringVar()
labelClickNumberText.set("Number of auto-clicks: ")

label3 = tk.Label(app, textvariable=labelClickNumberText)
label3.place(x=35, y=100)

spinBoxNum = tk.StringVar()
s = tk.Spinbox(app, from_ = 1, to = 250, textvariable=spinBoxNum)
s.place(x=65, y=100)

buttonImageSelectCheck1 = tk.Button(text="select image file to scan as fishing spot ", width=35, command=importImageSelection)
buttonImageSelectCheck1.place(x=35, y=150)

imageSelectLocationText = tk.StringVar()
imageSelectLocationText.set("")
label1 = tk.Label(app, textvariable=imageSelectLocationText)
label1.place(x=35, y=200)

selectionOneText = tk.StringVar()
selectionOneText.set("Direction of land (screen/not compass)")
label2 = tk.Label(app, textvariable=selectionOneText)
label2.place(x=35, y=250)

app.config()
app.mainloop()
