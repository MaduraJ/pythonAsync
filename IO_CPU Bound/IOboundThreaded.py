import requests,time,threading

def requestToExample():
	response=requests.get("https://example.com")
	print(response)
startTime=time.time()
print(f"Requests are sending {startTime}")
request1=threading.Thread(target=requestToExample)
request2=threading.Thread(target=requestToExample)
request3=threading.Thread(target=requestToExample)
request1.start()
request2.start()
request3.start()
request1.join()
request2.join()
request3.join()
endTime=time.time()
print(f'Total time spent {endTime-startTime:.4f}')