arr = [11,88,33,66,22,0,77,34,87]

def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]  
            else:
                pass
    
    print(arr)

selection_sort(arr)





# arr = [9, 1, 0, 2, 8, 3, 7, 4, 6, 5]

# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]  

# selection_sort(arr)
# print(arr)



