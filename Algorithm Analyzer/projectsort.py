# importing necessary modules

from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
#from mergesort import merge_sort
from mergesort import startMergeSort
from linearsearch import startLinearSearch
from binarysearch import startBinarySearch
#from shortestpath1 import main
#from shortpath import short

# creating the window for visualiser
root = Tk()
root.title('Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg = '#FAF2E8')
data = []



selected_algorithm = StringVar() 
# holds a string data where we can set text value and can retrieve it.
# here, it stores the algorithm which is to be performed


# starting the sorting process

def StartAlgorithm():
    global data
    if not data:
        return

    if(algo_menu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedscale.get())

    elif (algo_menu.get() == 'Bubble Sort'):
        bubble_sort(data, drawData, speedscale.get())

    elif (algo_menu.get() == 'Merge Sort'):
        startMergeSort(data, drawData, speedscale.get())
    elif (algo_menu.get() == 'Linear Search'):
        startLinearSearch(data, drawData, speedscale.get())
    elif (algo_menu.get()== 'Binary Search'):
        startBinarySearch(data, drawData, speedscale.get())
    #elif (algo_menu.get()== 'Shortest Path'):
     #   short()

    drawData(data, ['green'for x in range(len(data))])
    
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data =  [ i / max(data) for i in data]   # to get suitable size of the bars

    for i, height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i+1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
        canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]), font = ("times new roman", 15, "bold"),fill  = "orange")

    root.update_idletasks() #to visualise

# Generate function to generate the values for sorting
def Generate():
    global data
    print('Selected Algorithm: ' + selected_algorithm.get())

    minivalue = int(minvalue.get())
   
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue))
    drawData(data, ["#A90042" for x in range(len(data))])
# Main Label

label = Label(root, text = "Algorithm: ", font = ("times new roman", 16, "bold"), bg = "#AAC9CE",
            width = 10, fg = "black", relief = GROOVE, bd = 5)
label.place(x = 0, y = 0)


# menu for selecting algorithm

algo_menu = ttk.Combobox(root, width = 15, font =("times new roman", 19, "bold"), textvariable = selected_algorithm, values = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Linear Search', 'Binary Search'])
algo_menu.place(x = 145, y = 0)

# this will by default select the bubble sort algorithm
algo_menu.current(0)

random_generate = Button(root, text = "Generate", bg = "#FFBE88", font = ("times new roman", 12, "bold"), relief = SUNKEN,
activebackground = "#E8A49C", activeforeground = "white", bd = 5, width = 10,
command = Generate )
random_generate.place(x = 750, y = 60)

sizevaluelabel = Label(root, text = "Size: ", font = ("times new roman", 12, "bold"), bg = "#AAC9CE",
            width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
sizevaluelabel.place(x= 0, y = 60)

sizevalue = Scale(root, from_ = 0, to = 30, resolution = 1, orient = HORIZONTAL, font=("times new roman",14, "bold"),
                relief = GROOVE, bd = 2, width = 10)
sizevalue.place(x =120, y =60)



minvaluelabel = Label(root, text = "Min Value: ", font = ("times new roman", 12, "bold"), bg = "#AAC9CE",
            width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
minvaluelabel.place(x= 250, y = 60)

minvalue = Scale(root, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, font=("arial",14, "italic bold"),
                relief = GROOVE, bd = 2, width = 10)
minvalue.place(x =370, y =60)


maxvaluelabel = Label(root, text = "Max Value: ", font = ("times new roman", 12, "bold"), bg = "#AAC9CE",
            width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
maxvaluelabel.place(x= 500, y = 60)

maxvalue = Scale(root, from_ = 0, to = 100, resolution = 1, orient = HORIZONTAL, font=("times new roman",14, "bold"),
                relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x= 620, y =60)


start = Button(root, text = "Start", bg = "#56C596", font = ("times new roman", 12, "bold"), relief = SUNKEN,
activebackground = "#05945B", activeforeground = "white", bd = 5, width = 10 , command = StartAlgorithm)
start.place(x = 750, y = 0)

speedlabel = Label(root, text = "Speed: ", font = ("times new roman", 12, "bold"), bg = "#AAC9CE",
            width = 10, fg = "black", relief = GROOVE, bd = 5)
speedlabel.place(x= 400, y = 0)

speedscale = Scale(root, from_ = 0.1, to =5.0 , resolution = 0.2,length =  200, digits = 2, orient = HORIZONTAL, font=("times new roman",14, "bold"),
                relief = GROOVE, bd = 2, width = 10)
speedscale.place(x =520, y =0)

canvas = Canvas(root, width = 870, height = 450, bg = "#C9BBC8")
canvas. place(x = 10, y = 130)

root.mainloop()