import threading
import time

globalCount=0
class Count(threading.Thread):
	"""docstring for Count"""
	def __init__(self, CountTo,CountName):
		super().__init__()
		self.CountTo=CountTo
		self.CountName=CountName
		self.Mutex_lock=threading.Lock()

	#def returnCount(self):
		#return self.globalCount

	#def globalCountNow(self):
		#self.globalCount+=returnCount()
	def run(self):
		global globalCount
		print(f'Count {self.CountName} started counting to {self.CountTo}')
		#time.sleep(.1)
		while globalCount<self.CountTo:
			self.Mutex_lock.acquire()
			globalCount+=1
			self.Mutex_lock.release()
			print(f'Count {self.CountName} is currently at {globalCount}')
			if(globalCount>=self.CountTo):
				print(f"Counting {self.CountName} has finished at {globalCount}")
				break
	
if __name__ == '__main__':
	Count1=Count(1000,"Count 1")
	Count2=Count(1000,"Count 2")
	Count3=Count(1000, "Count 3")
	#StartTime=time.time()
	Count1.start()
	#EndTime=time.time()
	#Count1.join()
	#print(f'TimeSpent Count 1 {EndTime-StartTime:.4f}')
	#StartTime=time.time()
	Count2.start()
	#EndTime=time.time()
	#Count2.join()
	#print(f'TimeSpent Count 2 {EndTime-StartTime:.4f}')
	#StartTime=time.time()
	Count3.start()
	#EndTime=time.time()
	#Count3.join()
	#print(f'TimeSpent Count 2 {EndTime-StartTime:.4f}')
