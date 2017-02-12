# exceptionHandlers @ StirHack 2017
# James Waterhouse, Connor Stephen, Matty Burt, Jack Gilmore
# StirHack 2017

import bluetooth
import time
import sys
from Tkinter import *
from PIL import Image, ImageTk
import tkFont
import tkMessageBox

# Main method
def mainmethod():
    # Update current gui to display the labels
    v.set("Checking attendance...")
    o.delete(0,END)
    root.update()
    
    # Hardcoded MAC addresses    
    addrJames = '48:43:7C:9B:A2:BF'
    addrConnor = 'C0:EE:FB:D8:0B:C1'
    addrJack = '48:BF:6B:4B:84:11'
    addrJackBook = '20:C9:D0:E3:DB:02'
    addrMatty = 'BC:4C:C4:2C:B1:43'

    
    # DEBUG STRINGS    
    print "StirHack2017 - Check for attendance from known members"
    # List of hardcoded MAC addresses    
    knownHardcodedList = [addrJames, addrConnor, addrJack, addrJackBook, addrMatty]
    # Get nearby devices
    nearby_devices = bluetooth.discover_devices(lookup_names=True, flush_cache=False)
    # If the list of nearby devices is not empty    
    if len(nearby_devices) > 0:
        print "Collection of known members successful"
    # Else: if the list is empty        
    else:
        # Output and exit the program        
        print "Collection unsuccessful no users found"
        sys.exit("Registration Exited")
        
    # Initialize verified addresses array
    print nearby_devices
    verifiedAddresses = []

    # Loop through discovered devices
    for addr, name in nearby_devices:
        # Loop through hardcoded MACs
        for i in range(0, len(knownHardcodedList)):
            # If there is a match
            if knownHardcodedList[i] == addr:
                # Record attendance and break loop
                print name + " is currently attending"
                verifiedAddresses.append(name)
                break

    # While i is less than length of list
    i = 0
    for i in range(len(knownHardcodedList)):
        if knownHardcodedList[i] == "":
            knownHardcodedList.pop(i)
        else:
            continue
        i = i+1
    
    # DEBUG PRINT
    print verifiedAddresses
    
    # Output to label that we are finished
    v.set("Finished")
    
    # Loop through verified addresses to add them to the list box 
    for item in verifiedAddresses:
            o.insert(END, item)

def test(event):
    tkMessageBox.showinfo("DEBUG","DEBUG")

### GUI SETUP ###
root = Tk()

dictionary = {}
# Fonts
small = tkFont.Font(family="Arial", size=12)
medium = tkFont.Font(family="Arial", size=20)
large = tkFont.Font(family="Arial", size=36, weight="bold")

# GUI dimensions and location
w = 1800
h = 925
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# Label and list box packing and stuff
stirLabel = Label(root, text="Hello StirHack! Welcome to the show!",font=large)
stirLabel.pack()
image = Image.open("stirhack.png")
photo = ImageTk.PhotoImage(image)
photoLabel = Label(image = photo)
photoLabel.image = photo
photoLabel.pack()
v = StringVar()
o = Listbox(width=25,height=10,font=medium)
o.bind("<Double-1>", test)
o.pack()
Label(root, textvariable=v,font=medium).pack()
Label(root, text="", font=medium)
b = Button(root, text="Refresh devices", command=mainmethod)
b.pack()

# RUn main method after initializing GUI
root.after(0, mainmethod())
root.mainloop()
