import time  
def Count():
	y=0
	for x in range(100000000):
		y=x+x
	print(y)

print(f'Counting has started')
StartTime=time.time()
Count()
Count()
EndTime=time.time()
print(f'{EndTime-StartTime:.4f}')
