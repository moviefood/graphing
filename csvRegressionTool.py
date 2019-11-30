from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.interpolate import *
import csv
from pandas import *
#lolz
root = Tk()
root.wm_title("Regression Tool")

def firstFile():
    root.filename1 = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    firstFileStatus.config(state = tkinter.NORMAL)
    firstFileStatus.delete('1.0', END)
    firstFileStatus.insert(END, root.filename1)
    firstFileStatus.config(state=tkinter.DISABLED)

def secondFile():
    root.filename2 = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    secondFileStatus.config(state = NORMAL)
    secondFileStatus.delete('1.0', END)
    secondFileStatus.insert(END, root.filename2)
    secondFileStatus.config(state = DISABLED)

def regressionTool():

    regressionStatus.config(state=NORMAL)
    regressionStatus.delete('1.0', END)

    columnNames = ['x', 'y']

    try:
        data1 = pandas.read_csv(root.filename1, names=columnNames)
        data2 = pandas.read_csv(root.filename2, names=columnNames)

        bigData = data1.append(data2)

        x = bigData.x.tolist()
        y = bigData.y.tolist()

        gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        x_new = np.linspace(min(x), max(x), 200)

        f = interp1d(x, y, kind='quadratic')

        line = f(x_new)

        # plt.plot(x_new, line)

        mn = np.min(x)
        mx = np.max(x)

        x1 = np.linspace(mn, mx, 500)

        y1 = gradient * x1 + intercept

        plt.clf()
        plt.scatter(x, y)
        # plt.plot(x,y,'ob')
        plt.plot(x1, y1, '-r')
        # plt.plot(x_new, line)
        plt.show()
    except Exception:
        regressionStatus.insert(END, "You must select two CSV files.")

    regressionStatus.config(state=DISABLED)

firstFileButton = Button(root, text="Select First File", command=firstFile)
firstFileButton.grid(row = 0, sticky = W)

firstFileStatus = tkinter.Text(root, state = 'disabled', height = 1)
firstFileStatus.grid(row = 0, column = 1, columnspan = 2, sticky = E + W)

secondFileButton = Button(root, text="Select Second File", command=secondFile)
secondFileButton.grid(row = 1, sticky = W)

secondFileStatus = tkinter.Text(root, state = 'disabled', height = 1)
secondFileStatus.grid(row = 1, column = 1, columnspan = 2, sticky = E)

regressionButton = Button(root, text="View Regression Line", padx = 100, command=regressionTool)
regressionButton.grid(row = 2, columnspan = 3)

regressionStatus = tkinter.Text(root, state = 'disabled', height=1, width=60)
regressionStatus.grid(row = 3, columnspan = 2, sticky = W + E)

quitButton = Button(root, text="Quit", command=quit)
quitButton.grid(row = 3, column = 3, sticky = E + W)

mainloop()