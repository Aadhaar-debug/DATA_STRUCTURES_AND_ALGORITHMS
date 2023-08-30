x=0
y=5
for i in range(x,y):
    for j in range(x,y):
        if(i == x or i == y-1 or j == x or j == y-1):
            print("*  ",end="")
        else:
            print("   ",end="")
    print()


'''
THis code prints the below
*  *  *  *  *  
*           *
*           *
*           *
*  *  *  *  *
'''