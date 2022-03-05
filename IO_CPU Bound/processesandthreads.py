import os
import threading as th
import platform

try:
	print(f'Python process running with process id: {os.getpid()}')
	print(f'This is the Operating system Name : {platform.platform()}')
	print(f"Node :{platform.node()}")
	print(f"Machine :{platform.machine()}")
	print(f"processor :{platform.processor()}")
	print(f"python compiler:{platform.python_compiler()}")
	#print(f"platform U name: {0}",[platform.uname(),"node"])
	total_threads=th.active_count()
	thread_name=th.current_thread().name
	thread_list=th.enumerate()
	native_id=th.get_native_id()
	print(f"Currently running {total_threads} threads")
	print(f"Name of the current therad {thread_name}")
	print(f'\nThread List {thread_list}')
	print(f"Native id: {native_id}")
except Exception as e:
	print(e)
except OSError as e:
	print(e)
else:
	pass
finally:
	pass
