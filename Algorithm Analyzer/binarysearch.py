from time import sleep
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

#from random import randrange
colorData=[]

def startBinarySearch(data, drawData,stepTime):
    data=sorted(data)
    index_string = askstring('Index', 'Enter the index you want to check')
    index = int(index_string)
    colorData=['grey' for x in range(len(data))]
    colorData[index]='blue'
    start=0
    end=len(data)-1

    while start<end:
        mid = int((start+end)/2)
        drawData(data,colorData)
        sleep(stepTime)
        if data[index]>data[mid]:
            colorData[start:mid+1]=['red' for x in range(mid-start+1)]
            drawData(data,colorData)
            sleep(stepTime)
            start=mid+1
        elif data[index]<data[mid]:
            colorData[mid:end+1]=['red' for x in range(end-mid+1)]
            drawData(data,colorData)
            sleep(stepTime)
            end=mid-1
        else:
            break
    colorData[index]='green'
    showinfo('Search', 'Element found at index is {}'.format(data[index]))
    drawData(data,colorData)
    sleep(stepTime)