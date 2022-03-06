import requests,time

def requestToExample():
	response=requests.get("https://example.com")
	print(response)
startTime=time.time()
print(f"Requests are sending {startTime}")
requestToExample()
requestToExample()
requestToExample()
endTime=time.time()
print(f'Total time spent {endTime-startTime:.4f}')