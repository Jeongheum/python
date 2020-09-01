import numpy as np
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%b_%d_%Y")
#print("%b_%d_%Y",date_time)

fquiz=open('joony_quiz_'+ date_time +'.txt','w')
fans=open('joony_ans_'+ date_time + '.txt','w')

fquiz.write(date_time)
fquiz.write("\n")

fans.write(date_time)
fans.write("\n")

#fquiz.write(date_time)
for i in range(10):
    a=np.random.randint(1,10)
    b=np.random.randint(1,10)

    #print("%2d + %2d = %2d" %(a,b,a+b))
    fquiz.write("%2d) %2d + %2d = " %(i+1,a,b))
    fquiz.write("\n")
    fans.write("%2d) %2d + %2d = %2d" %(i+1,a,b,a+b))
    fans.write("\n")

fquiz.close()
fans.close()