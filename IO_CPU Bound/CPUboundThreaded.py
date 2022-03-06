import time, threading 
def Count():
	y=0
	for x in range(100000000):
		y=x+x
	print(y)
StartTime=time.time()
print(f'Counting has started')
count1=threading.Thread(target=Count)
count2=threading.Thread(target=Count)
count1.start()
count2.start()
count1.join()
count2.join()
EndTime=time.time()
print(f'Time spent {EndTime-StartTime:.4f}')