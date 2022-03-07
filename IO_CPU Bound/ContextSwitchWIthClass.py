import threading
import time

class Count(threading.Thread):
	"""docstring for Count"""
	def __init__(self, CountTo,CountName):
		super().__init__()
		self.CountTo=CountTo
		self.CountName=CountName

	def run(self):
		print(f'Start {self.CountName} Counting to {self.CountTo}')
		time.sleep(.1)
		x=0
		while x<self.CountTo:
			x=x+1
			print(f'Current {self.CountName} is at {x}')
			time.sleep(.1)
			if(x>=self.CountTo):
				break
		print(f"Counting {self.CountName} has finished at {x}")
	
if __name__ == '__main__':
	Count1=Count(100,"Count 1")
	Count2=Count(100,"Count 2")
	Count3=Count(100, "Count 3")
	StartTime=time.time()
	Count1.start()
	EndTime=time.time()
	#Count1.join()
	print(f'TimeSpent Count 1 {EndTime-StartTime:.4f}')
	StartTime=time.time()
	Count2.start()
	EndTime=time.time()
	#Count2.join()
	print(f'TimeSpent Count 2 {EndTime-StartTime:.4f}')
	StartTime=time.time()
	Count3.start()
	EndTime=time.time()
	#Count3.join()
	print(f'TimeSpent Count 2 {EndTime-StartTime:.4f}')
