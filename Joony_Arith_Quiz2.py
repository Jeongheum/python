import numpy as np

score = 0
for i in range(10):
    a=np.random.randint(1,10)
    b=np.random.randint(1,10)

    #print("%2d + %2d = %2d" %(a,b,a+b))
    y=input("%2d) %2d + %2d = " %(i+1,a,b))

    if int(y) == (a+b):
        score = score +10
        print("Excellent !  %2d + %2d = %2d" %(a,b,a+b))
    else:
        print("Wrong ! %2d + %2d = %2d" %(a,b,a+b))

print ("\n Your score is %d"%(score))