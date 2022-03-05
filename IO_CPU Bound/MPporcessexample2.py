from multiprocessing import Process
import threading
import os

def cpu_waster():
	while True:
		pass
print(f'Parent process ID {os.getppid()} !')
print(f'Process ID: {os.getpid()} !')
print(f'Active thread count: {threading.active_count()} !')
print(f'Current thread {threading.current_thread()}')

if __name__ == '__main__':
	cpu_waster_process_count=6
	for processes in range(cpu_waster_process_count):
		cpuwaster_process=Process(target=cpu_waster).start()
		print(f'\n Process id {os.getpid()} \n')
		print(f'Parent process ID {os.getppid()} !')
	
	print(f'Active thread count: {threading.active_count()} !')
	print(f'Current thread {threading.current_thread()}')