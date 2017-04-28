# this is the main engine script for the app

# some imports
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

# defining some classes here
class mainWindow:
    '''This is the calss for main app window'''

    def __init__(self, master, lineup=[]):

        # Setting up some object variables
        self.master = master
        self.lineup = lineup

        # starting work with tkinter interface
        # setting up first frame element with 5pixels distances around
        self.frame_top = tk.Frame(self.master)
        self.frame_top.pack(padx=5, pady=5)

        # now we add some text on the very top
        self.topBaner = tk.Label(self.frame_top,
                                 text='Welcome to the lineup creator!',
                                 font=20)

        self.topBaner.grid(row=0, column=0, columnspan=10)

        # second frame element to keep middle part together
        self.frame_mid = tk.Frame(self.master)
        self.frame_mid.pack(padx=5, pady=5)

        # so we add a canvas element here
        self.canvas = tk.Canvas(self.frame_mid, width=800, height=250,
                                background='white')
        self.canvas.grid(row=0, column=0)

        # bottom frmae to keep controls under canvas
        self.frame_btm = tk.Frame(self.master)
        self.frame_btm.pack(padx=5, pady=5)

        self.addButton = tk.Button(self.frame_btm, text='Hellow',
                                   command=self.onClick)
        self.addButton.grid(row=0, column=0, columnspan=10)

    def addImageToCanvas(self, image_file, x=0, y=0):
        '''This procedure prints out image file to the window canvas'''
        # Load the image file
        im = Image.open(image_file)
        # Let's resize it to fit our canvas size
        canvasX = self.canvas.winfo_width()
        canvasY = self.canvas.winfo_height()

        imageX, imageY = im.size

        if imageY > canvasY:
            imageX = int(imageX * (canvasY / imageY))
            imageY = int(canvasY)

        size = imageX, imageY


        im = im.resize(size, Image.ANTIALIAS)
        # Put the image into a canvas compatible class, and stick in an
        # arbitrary variable to the garbage collector doesn't destroy it
        self.canvas.image = ImageTk.PhotoImage(im)
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

    def onClick(self):
        self.addImageToCanvas(image_file='/home/tomasz/Dropbox/Git/WhoPy/04_tkinter_02_appbuild/img/entelleon.png')
        print('Adding image')

# Here is where the main app starts
if __name__ == '__main__':
    '''This is the main loop executed if script is run directly'''

    # Defining the main tkinter master window object (parent to all windows)
    root = tk.Tk()
    root.title('Lineup Creator')
    mW = mainWindow(root)

    # looping the script to wait till the GIU is closed by user
    root.mainloop()
