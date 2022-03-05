import threading, os

try:
	print(f'parent process ID: {os.getppid()}')
	print(f"hello form the process {os.getpid()}")
	print(f'Current thread count : {threading.active_count()}')

	def hello_from_thread():
		thread_name=threading.current_thread()
		print(f'Hello from thread {thread_name} !')
	def hello_from_thread2():
		thread_name=threading.current_thread()
		print(f'Hello from thread {thread_name} !')
	def hello_from_thread3():
		thread_name=threading.current_thread()
		print(f'Hello from thread {thread_name} !')
	
	hello_thread=threading.Thread(target=hello_from_thread)
	hello_thread.start()
	print(f'Current thread count : {threading.active_count()}')
	print(f"hello_thread is {hello_thread.is_alive()}")

	hello_thread2=threading.Thread(target=hello_from_thread2)
	hello_thread2.start()
	print(f'Current thread count : {threading.active_count()}')
	print(f"hello_thread 2 is {hello_thread2.is_alive()}")

	hello_thread3=threading.Thread(target=hello_from_thread3)
	hello_thread3.start()
	print(f'Current thread count : {threading.active_count()}')
	print(f"hello_thread 3 is {hello_thread3.is_alive()}")

	total_thrads=threading.active_count()
	print(f"Python is currently rnning active {total_thrads} thread(s)")

	thread_name=threading.current_thread().name
	print(f"The current thread is {thread_name}")

	

	for threads in threading.enumerate():
		print(f'\n {threads} \n')

	
	
	#print(f"Thread enumerate \n {threading.enumerate()}")

	hello_thread.join()
	hello_thread2.join()
	hello_thread3.join()
except Exception as e:
	raise
else:
	pass
finally:
	pass
