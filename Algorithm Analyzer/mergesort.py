#import time
"""
def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data)-1, drawData, timeTick)



def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):

    drawData(data, colorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftpart = data[left: middle+1]
    rightpart = data[middle+1: right+1]

    leftIdx =  rightIdx = 0

    for dataIdx in range(left,right):
        
        if leftIdx < len(leftpart) and rightIdx < len(rightpart):
            if leftpart[leftIdx] <= rightpart[rightIdx]:
                data[dataIdx] = leftpart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightpart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftpart):
            data[dataIdx] = leftpart[leftIdx]
            leftIdx +=1
        else:
            data[dataIdx] = rightpart[rightIdx]
            rightIdx += 1
    
    drawData(data,["green" if x >= left and x <=right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def colorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <=middle:
                colorArray.append('yellow')
            else:
                colorArray.append("orange")

        else:
            colorArray.append("white")
    return colorArray
    
"""

from time import sleep


def startMergeSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    mergeSort(data,0,len(data)-1,drawData,stepTime)
    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)


def merge(data,start,end,drawData,stepTime):
    i=start
    j=(start+end)//2+1
    a=[]
    while i<=(start+end)//2 and j<=end:
        colorData[i]=colorData[j]='blue'
        drawData(data,colorData)
        colorData[i]=colorData[j]='grey'
        sleep(stepTime)
        if data[i]<data[j]:
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[i]='grey'
            a.append(data[i])
            i+=1
        else:
            colorData[j]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='grey'
            a.append(data[j])
            j+=1
    
    while i<=(start+end)//2:
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[i]='grey'
        a.append(data[i])
        i+=1
    
    while j<=end:
        colorData[j]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j]='grey'
        a.append(data[j])
        j+=1
    for x in range(start,end+1):
        data[x]=a[x-start]



def mergeSort(data,start,end,drawData,stepTime):
    
    if start>=end:
        return

    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]


    mergeSort(data,start,(start+end)//2,drawData,stepTime)
    mergeSort(data,(start+end)//2+1,end,drawData,stepTime)
    merge(data,start,end,drawData,stepTime)


    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]
    # for x in range(start,end+1):
    #     drawData(data,colorData)
    #     sleep(stepTime)