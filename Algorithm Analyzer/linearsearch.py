from time import sleep
#from random import randrange
#from tkinter import simpledialog
#from tkinter import messagebox
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

colorData=[]

def startLinearSearch(data, drawData,stepTime):
    #index=randrange(0,len(data))
    index_string  = askstring('Index', 'Enter the index you want to check')
    index = int(index_string)
    colorData=['grey' for x in range(len(data))]
    for x in range(len(data)):
        if data[x]==data[index]:
            colorData[x]='blue'
            break
    for i in range(len(data)):
        colorData[i]='white'
        drawData(data,colorData)
        sleep(stepTime)
        if data[i]==data[index]:
            colorData[i]='green'
            drawData(data,colorData)
            showinfo('Search', 'Element found at index is {}'.format(data[i]))
            sleep(stepTime)
            break
        else:
            colorData[i]='red'
            sleep(stepTime)
