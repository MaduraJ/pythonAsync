import time
from multiprocessing import Process 
def Count():
	y=0
	for x in range(100000000):
		y=x+x
	print(y)
if __name__ == '__main__':
	StartTime=time.time()
	print(f'Counting has started')
	count1=Process(target=Count)
	count2=Process(target=Count)
	count1.start()
	count2.start()
	count1.join()
	count2.join()
	EndTime=time.time()
	print(f'{EndTime-StartTime:.4f}')