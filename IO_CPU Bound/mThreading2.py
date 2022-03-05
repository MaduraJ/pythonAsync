import threading, os

def cpu_waster():
	while True:
		pass

print(f'Thread count {threading.active_count()}')
print(f'Current Thread name : {threading.current_thread().name}')
print(f'Parent process id {os.getppid()}')
print(f'Process id {os.getpid()}')

cpuwater_count=4
print(f"starting {cpuwater_count} Thread(s)")


for Thread in range (cpuwater_count):
	CPUwaster=threading.Thread(target=cpu_waster).start()
	print(f'{threading.current_thread()}')

print(f'Thread count {threading.active_count()}')
print(f'Current Thread name : {threading.current_thread().name}')
for Threads in threading.enumerate():
	print(Threads)


