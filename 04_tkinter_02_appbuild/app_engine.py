# this is the main engine script for the app

# some imports
import tkinter as tk
import numpy as np
# import matplotlib.pyplot as plt
from PIL import ImageTk, Image

# defining some classes here
class mainWindow:
    '''This is the calss for main app window'''

    def __init__(self, master, lineup=[]):

        # Setting up some object variables
        self.master = master
        self.lineup = lineup

        self.naszeX = 0

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

        # # so we add a canvas element here
        # self.canvas = tk.Canvas(self.frame_mid, width=500, height=250,
        #                         background='white')
        # self.canvas.grid(row=0, column=0)

        # bottom frmae to keep controls under canvas
        self.frame_btm = tk.Frame(self.master)
        self.frame_btm.pack(padx=5, pady=5)

        self.addButton = tk.Button(self.frame_btm, text='Hellow',
                                   command=self.onClick)
        self.addButton.grid(row=0, column=0, columnspan=10)

    def addImageToCanvas(self, c, image_file, x=0, y=0):
        '''This procedure prints out image file to the window canvas'''
        # Load the image file
        im = Image.open(image_file)
        im = im.resize((100,100))
        # # Let's resize it to fit our canvas size
        # to the garbage collector doesn't destroy it
        c.image = ImageTk.PhotoImage(im)
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        c.create_image(x, y, image=c.image, anchor='nw')
        print('Adding image na: {} {}'.format(x, y))

    def onClick(self):

        self.canvas = []
        for szafa in self.lineup:
            # so we add a canvas element here
            self.canvas.append(tk.Canvas(self.frame_mid, width=100, height=250,
                                    background='white'))

            self.canvas[-1].grid(row=0, column=self.naszeX)

            self.addImageToCanvas(c=self.canvas[-1], image_file='img/entelleon.png')
            self.naszeX += 100


# Here is where the main app starts
if __name__ == '__main__':
    '''This is the main loop executed if script is run directly'''

    # Defining the main tkinter master window object (parent to all windows)
    root = tk.Tk()
    root.title('Lineup Creator')
    mW = mainWindow(root, [1])

    # root2 = tk.Tk()
    # root2.title('Drugi')
    # mW2 = mainWindow(root2)

    # print(mW2.lineup)
    # looping the script to wait till the GIU is closed by user
    root.mainloop()
