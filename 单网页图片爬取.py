import requests
from bs4 import BeautifulSoup
import os

def getHTML(url):
	try:
		kv={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
		r=requests.get(url,headers = kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print('爬取失败')

def getURL(html,ulist):
	soup = BeautifulSoup(html,'html.parser')
	alist = soup.find_all('img',attrs={'alt':'轮椅篮球：生命中的一道光'})
	# alist = soup.find('div','tab_imgs js_carousel').find('ul')#找到对应标签及属性值
	# for img in alist.find_all('img'):#子标签
	# 	ulist.append(img.get('src'))#图片链接添加到列表
	for scr in alist:
		ulist.append(scr.get('src'))
	


def downloand(url):
	root='C:/Users/阳/Desktop/pics'
	path = root+url.split('/')[-1]
	print(path)
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			r = requests.get(url)
			r.raise_for_status()
			with open(path,'wb')as k:
				k.write(r.content)
				k.close()
				print('文件保存成功')
		else:
			print('文件已存在')
	except:
		print('失败')


def main():
	ulist = []
	url = 'http://www.ngchina.com.cn/culture/9392.html'
	html = getHTML(url)
	getURL(html,ulist)
	for k in ulist:
		downloand(k)
		print('finish')

main()



################### 爬取大图
import requests
from bs4 import BeautifulSoup
import re
import os

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('解析失败')

def get_image(html):

    # images_url = re.findall('<img src=".*?" data-lazy-srcset=".*?" data-lazy="(.*?)" alt=',html,re.S)

    # for img in images_url:
    #     imgs = img.split('__')[0]+'_960_720.jpg'
    #     ulist.append(imgs)
    # return ulist

    u_url = re.findall('<img src=".*?" data-lazy-srcset=".*?" data-lazy="(.*?)" alt=',html,re.S)
    
    images_url=[]

    for img_url in u_url:
        imgs = img_url.split('__')[0]+'_960_720.jpg'#大图地址

        images_url.append(imgs)

    return images_url

    # <img srcset=".*?" src="(.*?)" alt=

    # '<img src=".*?" data-lazy-srcset=".*?" data-lazy="(.*?)" alt='

def down_img(img_urls):

    for img_url in img_urls:
        root = 'D:/image/'
        path = root+img_url.split('/')[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(img_url)
            with open(path,'wb')as f:
                f.write(r.content)
                print('保存成功')
        else:
            print('图片存在')

def main():

    urls = ['https://pixabay.com/zh/images/search/?pagi={}'.format(str(i)) for i in range(1,3)]
    
    for url in urls:
        html = gethtml(url)
        img_urls=get_image(html)

        down_img(img_urls)

main()