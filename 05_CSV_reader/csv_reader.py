# this is a project to create a pandas based
# CSV files reader and plotter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd

# lets define some class here
class MainWindow:
	def __init__(self, master):

		self.master = master
		self.frame = tk.Frame(self.master)
		self.frame.pack(padx=5, pady=5)

		self.openButton = tk.Button(self.frame, text='Open CSV', command=self.openFile)
		self.openButton.pack()

	def openFile(self):
		print('Im openning a file now')
		filename = fd.askopenfilename(filetypes=[("CSV files", "*.csv")])
		if filename is not '':
			self.readCSV(filename)
		else:
			print('No file selected')

	def readCSV(self, filename):
		try:
			df = pd.read_csv(filename)
		except:
			print('File {} opening issue'.format(filename))
		else:
			print(df.head())
			df = df.replace({',': '.'}, regex=True)
			df = df.astype(float)
			df.set_index('Time [s]', inplace=True)
			print(df.head())
			self.plotCSV(df)

	def plotCSV(self, df):
		df.plot()
		plt.show()

# Here is where the main app starts
if __name__ == '__main__':
	root = tk.Tk()
	root.title('CSV reader')
	mW = MainWindow(root)
	root.mainloop()
