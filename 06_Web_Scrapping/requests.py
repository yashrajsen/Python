import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.status_code   #404- Not Found; 200 - everything loaded OK
#print(res) 
print(res.text[:500])
#x = requests.get('https://w3schools.com/python/demopage.htm', auth=('user', 'pass'))

#print(x.text) 