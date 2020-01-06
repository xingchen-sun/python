import requests
import csv 
from bs4 import BeautifulSoup
import bs4
import re

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('解析失败')


def pagelist(ulist,html):
    soup = BeautifulSoup(html,'html.parser')

    alist = alist = soup.find('tbody')
    for tr in alist.children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), 
                tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text(), tds[9].get_text(), tds[10].get_text(), 
                tds[11].get_text(), tds[12].get_text(), tds[13].get_text(), tds[14].get_text(), tds[15].get_text(),tds[-3].get_text(),tds[-2].get_text(),tds[-1].get_text()])

def printlist(ulist):
    tlpt='{:5}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:10}\t{:2}\t{:12}\t{:2}\t{:10}\t{:2}\t{:10}\t{:10}\t{:10}\t{:10}'
    print(tlpt.format('期数','红1','红2','红3','红4','红5','蓝1','蓝2','一等','奖金','追加','奖金','二等','奖金','追加','奖金','销售额','奖池金额','开奖日期'))

    for k in ulist:
        print(tlpt.format(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[10],k[11],k[12],k[13],k[14],k[15],k[16],k[17],k[18]))
        

        

def main():

    urls = ['https://www.lottery.gov.cn/historykj/history_{}.jspx?_ltype=dlt'.format(str(i)) for i in range(1,97)]

    ulist = []

    for url in urls:
        html=gethtml(url)
        pagelist(ulist,html)
    printlist(ulist)

main()



#爬取并存储为csv格式
import requests
import csv 
from bs4 import BeautifulSoup
import bs4



def create_csv_header():
    with open('dlt.csv','a',encoding='gbk',newline='')as f:#encoding 编码'utf-8'乱码修改成'gbk'
        writer = csv.writer(f)
        writer.writerow(['期数','红1','红2','红3','红4','红5','蓝1','蓝2','一等注数','奖金金额','追加注数','奖金金额','二等注数','奖金金额','追加注数','奖金金额','销售额','奖池金额','开奖日期'])

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('解析失败')


def pagelist(html):
    soup = BeautifulSoup(html,'html.parser')

    ulist = []

    alist = alist = soup.find('tbody')
    for tr in alist.children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), 
                tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text(), tds[9].get_text(), tds[10].get_text(), 
                tds[11].get_text(), tds[12].get_text(), tds[13].get_text(), tds[14].get_text(), tds[15].get_text(),tds[-3].get_text(),tds[-2].get_text(),tds[-1].get_text()])
    return ulist#返回列表

# def printlist(ulist):
#     tlpt='{:5}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:10}\t{:2}\t{:12}\t{:2}\t{:10}\t{:2}\t{:10}\t{:10}\t{:10}\t{:10}'
#     print(tlpt.format('期数','红1','红2','红3','红4','红5','蓝1','蓝2','一等','奖金','追加','奖金','二等','奖金','追加','奖金','销售额','奖池金额','开奖日期'))

#     for k in ulist:
#         print(tlpt.format(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[10],k[11],k[12],k[13],k[14],k[15],k[16],k[17],k[18]))
        
def write_csv(data):
    with open('dlt.csv','a+',encoding='gbk',newline='') as f:
        writer = csv.writer(f)
        for _ in data:
            writer.writerow(_)



def main():

    urls = ['https://www.lottery.gov.cn/historykj/history_{}.jspx?_ltype=dlt'.format(str(i)) for i in range(1,5)]
    create_csv_header()

    for url in urls:
        html=gethtml(url)
        data=pagelist(html)
        write_csv(data)
    print("存储完成")

main()

