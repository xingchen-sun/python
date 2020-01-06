
import requests
from bs4 import BeautifulSoup

def getHtml(url):
	try:
		kv = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
		r = requests.get(url,headers = kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print('爬取失败')

def pageMu(ulist,html):
	soup = BeautifulSoup(html,'html.parser')

	alist = soup.find_all('tr','alt')

	for info in alist:
		nums = info.find_all('td')[0].get_text()
		nams = info.find_all('td')[1].get_text()
		shenf=info.find_all('td')[2].get_text()
		scors=info.find_all('td')[3].get_text()
		
		ulist.append([nums,nams,shenf,scors])

def printList(ulist):
	tplt ='{:5}\t{:35}\t{:10}\t{:5}'
	print(tplt.format('排名','学校名称','身份','总分',chr(12288)))
	for g in ulist:
		print(tplt.format(g[0],g[1],g[2],g[3]),chr(12288))



def main():
	url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
	infolist = []

	html = getHtml(url)
	pageMu(infolist,html)

	printList(infolist)

main()