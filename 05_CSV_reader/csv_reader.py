# this is a project to create a pandas based
# CSV files reader and plotter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.simpledialog import askstring as astr

matplotlib.use('TkAgg')


# lets define some class here
class MainWindow:
    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=50, pady=50)

        self.openButton = tk.Button(self.frame, text='Open CSV',
                                    command=self.openFile)
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
            self.csvWindow(df, filename)

    def csvWindow(self, df, filename):
        root = tk.Tk()
        root.title('CSVr: {}'.format(filename))
        dfWindow(root, df)

    def plotCSV(self, df):
        df.plot()
        plt.show()

    def console(self, string):
        self.tx1.insert(tk.END, str(string))


class dfWindow:
    def __init__(self, master, df):
        self.master = master
        self.df = df
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=5, pady=5)

        self.tx1 = tk.Text(self.frame)
        self.tx1.pack()

        self.openButton = tk.Button(self.frame, text='Convert to Numbers', command=self.fixComma)
        self.openButton.pack()

        self.openButton = tk.Button(self.frame, text='Drop Column', command=self.dropDataColumn)
        self.openButton.pack()
        
        self.openButton = tk.Button(self.frame, text='Drop Rows', command=self.dropDataRow)
        self.openButton.pack()

        self.openButton = tk.Button(self.frame, text='Set Index Column', command=self.setAsIndex)
        self.openButton.pack()

        self.openButton = tk.Button(self.frame, text='Plot CSV', command=self.plotCSV)
        self.openButton.pack()

        self.console(self.df.head())

    def plotCSV(self):
        self.console('\n--Trying to plot the data-----\n')
        try:
            self.df.plot()
            plt.show()
        except:
            self.console('Problem with plotting. Check if data are numbers!\n')
            self.console(self.df.head())

    def fixComma(self):
        output = ''
        try:
            self.df.replace({',': '.'}, regex=True, inplace=True)
        except BaseException as e:
            output += str(e)
        try:
            self.df = self.df.astype(float)
        except BaseException as e:
            output += str(e)

        self.console('\n--Trying to convert to numbers & fixing commas ----\n')
        self.console(output+'\n')
        self.console(self.df.head())

    def dropDataColumn(self):
        columnName = astr('Delete Data Column',
                          'The name of column to drop (use : to separate if many):')
        columnName = columnName.split(':')
        output = ''
        for cName in columnName:
            try:
                self.df.drop([cName], axis=1, inplace=True)
            except BaseException as e:
                output += str(e)

        self.console('\n--Trying to delete column {} ---\n'.format(columnName))
        self.console(output+'\n')
        self.console(self.df.head())

    def dropDataRow(self):
        rowName = astr('Delete Data Rows',
                       'The range of rows to delete FROM:TO')
        
        if rowName is not None and rowName is not '':
            rowName = rowName.split(':')
            rowName = [int(x) for x in rowName]
            rName = [x for x in range(min(rowName), max(rowName)+1)]
        
        output = ''
        try:
            self.df.drop(self.df.index[rName], inplace=True)
            self.df.reset_index(drop=True, inplace=True)
        except BaseException as e:
            output += str(e)

        self.console('\n--Trying to delete row {} ---\n'.format(rowName))
        self.console(output+'\n')
        self.console(self.df.head())

    def setAsIndex(self):
        columnName = astr('Set Index Column', 'The name of column to be used as index:')
        output = ''
        try:
            self.df.set_index([columnName], inplace=True)
        except BaseException as e:
            output += str(e)
        self.console('\n--Trying to ser column {} as index ---\n'.format(columnName))
        self.console(output+'\n')
        self.console(self.df.head())

    def console(self, string):
        self.tx1.insert(tk.END, str(string))
        self.tx1.see(tk.END)

# Here is where the main app starts
if __name__ == '__main__':
    root = tk.Tk()
    root.title('CSV reader')
    mW = MainWindow(root)
    root.mainloop()
