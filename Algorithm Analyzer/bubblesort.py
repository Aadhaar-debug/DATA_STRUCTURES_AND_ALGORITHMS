import time


def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)- 1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] #swapping values
                drawData(data, ['grey'if x == j  or x ==j+1 else "white" for x in range(len(data))])
                time.sleep(timeTick)   # to select time as per need from the speed scale
    drawData(data, ['yellow' for x in range(len(data))])