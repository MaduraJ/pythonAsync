import requests,time
from multiprocessing import Process

def requestToExample():
	response=requests.get("https://example.com")
	print(response)
if __name__ == '__main__':
	startTime=time.time()
	print(f"Requests are sending {startTime}")
	request1=Process(target=requestToExample)
	request2=Process(target=requestToExample)
	request3=Process(target=requestToExample)
	request1.start()
	request2.start()
	request3.start()
	request1.join()
	request2.join()
	request3.join()
	endTime=time.time()
	print(f'Total time spent {endTime-startTime:.4f}')
