import re
import requests
from bs4 import BeautifulSoup

url="http://www.arghyabiswas.com/work"
html_doc=requests.get(url).text
a=url.split("/")
if a[0]=='http:' or a[0]=='https:':
	host=a[0]+"//"+a[2]
else:
	host=a[0]

print("\n\nhost:"+host+"\n\n")
soup = BeautifulSoup(html_doc, 'html.parser')
links=[]
for i in soup.find_all('a'):
	#print(i)
	href = i.get('href')
	if href != None and href != "#":
		if href not in links:
			links.append(href)

index=0
for link in links:
	if re.findall(host,str(link)):
		pass
	elif link.startswith("http"):
		pass
	else:
		links[index]=(host+"/"+str(link))
	index += 1

for i in links:
	#pass
	print(i)	
	

