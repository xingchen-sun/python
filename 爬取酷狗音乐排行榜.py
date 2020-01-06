
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
	nums = soup.find_all('span','pc_temp_num')
	names=soup.find_all('a','pc_temp_songname')
	times = soup.find_all('span','pc_temp_time')

	for num,name,time in zip(nums,names,times):
		nu =(num.get_text().replace('\n','').replace('\t','').replace('\r',''))
		na=(name.string)
		pna = na.split('-')[0]
		mna = na.split('-')[1]
		t =(time.get_text().replace('\n','').replace('\t','').replace('\r',''))
		ulist.append([nu,pna,mna,t])


def printList(ulist):
	tplt ='{:5}\t{:20}\t{:50}\t{:5}'
	print(tplt.format('排名','歌手','歌名','时间',chr(12288)))
	for g in ulist:
		print(tplt.format(g[0],g[1],g[2],g[3]),chr(12288))



def main():
	# url='https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
	urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,5)]
	
	infolist = []
	
	for url in urls:
		html = getHtml(url)
		pageMu(infolist,html)

	printList(infolist)

main()