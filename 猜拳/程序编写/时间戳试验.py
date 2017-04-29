import time
count=0
t1=time.time()
"""
time0=5

while(count<time0):
    order=input()
    if (order!=''):
        break
    ncount=time0-count
    #print(ncount)
    time.sleep(1)
    count+=1
else:
    print("超时！")
    """
order=input()
t2=time.time()
if(int(t2-t1)>5):
    print("超时！")
