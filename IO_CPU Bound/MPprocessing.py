from multiprocessing import Process
import os

def hello_from_process():
	print(f'Hello from the child process {os.getpid()} !')

if __name__== '__main__':
	Hello_process=Process(target=hello_from_process)
	Hello_process.start()
	print(f"Hello from main process {os.getpid()}")
	Hello_process.join()

