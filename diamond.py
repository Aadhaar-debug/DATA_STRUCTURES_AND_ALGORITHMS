x=8
y=8

for i in range(0,x):
    print("   "*x + ("*     " * i))
    x-=1


for j in range(0,y):
    print("   "*j + ("*     " * y))
    y-=1


'''
the above code prints the following 

                     *
                  *     *
               *     *     *
            *     *     *     *
         *     *     *     *     *
      *     *     *     *     *     *
   *     *     *     *     *     *     *
*     *     *     *     *     *     *     *
   *     *     *     *     *     *     *
      *     *     *     *     *     *
         *     *     *     *     *
            *     *     *     *
               *     *     *
                  *     *
                     *
'''