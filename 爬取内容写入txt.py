import requests
import re
from bs4 import BeautifulSoup
import csv

# def creat_csv():
#     with open('xs.csv','a',encoding ='gbk',newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['标题'])

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('解析失败')

def pagelist(html):
    path = '<dd><a href ="(.*?)">.*?</a></dd>'
    alists =re.findall(path,html,re.S)
    urls = []
    for i in alists[0:12]:
        url = 'https://www.biqukan.com'+i
        urls.append(url)
    
    return urls

# url= 'https://www.biqukan.com/0_790/'
# html = gethtml(url)
# urls = pagelist(html)

# for url in urls:
#     clist = []


#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     soup = BeautifulSoup(r.text,'html.parser')
#     blist = soup.find('div',attrs={'id':'content'}).get_text()   
    
#     clist.append(blist)
#     print(clist) 

# def write_csv(data):
#     with open('xs.csv','a+',encoding='gbk',newline='') as f:
#         writer = csv.writer(f)
#         for _ in data:
#             writer.writerow(_)

def jiexi(urls):
    for url in urls:
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            
        except:
            print('解析错误')

        soup = BeautifulSoup(r.text,'html.parser')
        hs = soup.find('h1').get_text()
        blist = soup.find('div',attrs={'id':'content'}).get_text()
        f = open("b.txt", 'w+')

        print(hs,file=f)#file = f 写入txt,如遇特殊字符可能报编码'gbk'错误
        print('&&&&'*20,file=f)
        print(blist,file=f)
        print('&&&&'*20,file=f)


        # blist = soup.find('div',attrs={'id':'content'}).get_text()
        # clist.append(blist)
        # print(clist)


def main():
    url= 'https://www.biqukan.com/0_790/'
    html = gethtml(url)
    urls = pagelist(html)
    jiexi(urls)

    print('写入完成')

main()





##############存入txt

name ='python常用的读取文件函数有三种read()、readline()、readlines() '
f = open("name.txt", "w+")
f.write(name)#写入只能写入字符串，不能是列表
print(name, file=f)#打印并写入



