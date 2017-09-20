"""
Created 9/06/2017
- 15 years after the creation of Slegger...

FishyFish.py

"So Long and Thanks for All the Fish"

"""

# import the goodies
import glob # to get list of file names as images for screenshots to know wher to click
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
    # where (location) the program can find our scrreenshot image
    #pyautogui.locateOnScreen(r'c:\temp\outbound\calc7key.png')
    ### <--- DO LOOPS AND CHECK UNTIL THAT PICTURE "is found"
    print (str(pyautogui.locateOnScreen(r'c:\temp\fish1.png')))
    return

def importImageSelection():

    app.imageSelect = filedialog.askopenfilename(initialdir = "C:\"", title="import IMAGE select", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg"), ("all files", "*.*")))
    imageSelectLocation = str(app.imageSelect)
    # set variable above to tk.string
    imageSelectLocationText.set(imageSelectLocation)
    # take from tk.string and set it to search for that screenshot
    print (str(pyautogui.screenshot(imageSelectLocationText.get())))
    return

app = tk.Tk()
app.title('FishyFish.exe')
app.geometry('400x400+200+200')

buttonBeginFish = tk.Button(app, text="So Long and Thanks for All the Fish", width=50, command=testFish)
buttonBeginFish.pack()

## INCLUDE BUTTON FOR 'AUTO' AND 'MANUAL' FOR FISHING SPOTS
buttonAlphaRun = tk.Button(app, text="Alpha RUN", width =20, command=alphaRun)
buttonAlphaRun.pack()

buttonImageSelectCheck1 = tk.Button(text="select image file to scan as fishing spot ", width=90, command=importImageSelection)
buttonImageSelectCheck1.place(x=35, y=150)

imageSelectLocationText = tk.StringVar()
imageSelectLocationText.set("")
label = tk.Label(app, textvariable=imageSelectLocationText)
label.place(x=35, y=200)

app.config()
app.mainloop()
