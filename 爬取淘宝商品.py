import requests
import re
 
def getHTMLText(url):
    try:
        kv={'cookie':'miid=1440918999221809251; cna=Iu7gFShe6WQCAWVQjarnMRca; t=3c3ededfc3940a772b58f053b83ab55e; tracknick=beichenriyue; tg=0; enc=%2FYqS6lF%2B%2FgaJzgPGMEnJ0O5h7zCk6qBLqRDZBL5bgynCjcAO9Miqn1HJs%2BmzntHmRIgVfbD8uBEKQs6DKNzl6g%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=16e1fa55d3c551-08774bad1f878b-6a19127e-100200-16e1fa55d3d51a; _cc_=W5iHLLyFfA%3D%3D; v=0; cookie2=76e5ba244e573e8cefc1e350ad5f85d4; _tb_token_=7a3b471ee835e; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=0A0093A3094637BDE5C45092A3534D33; l=dBTPI_Ocqze-BolOBOfgtuIRhL_O1IOf1sPzw4wghICPOV1eneZFWZLpO4LwCnGVHspWR3Skor_UBrLRayCI0m2ZB3k_J_qS3dC..; isg=BI-P0Ye0DnpcgQolIXJQOmVOHiNZHOlEp1y5V6GdR_5RcKxyqYD8Ju0pcuDrCLtO','user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        #头部加入cookie

        r = requests.get(url, headers = kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#正则表达价格
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)#*?最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#eval:去除引号
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0#序号
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = '书包'
    depth = 3#页数
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()