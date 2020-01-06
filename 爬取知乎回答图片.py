import requests
import re
import time
import os


def getHTMltext(url_, header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;'
                              'Win64; x64) AppleWebKit/537.36 (KHTML, like'
                              'Gecko) Chrome/69.0.3497.100'
                              'Safari/537.36','Referer': "https://www.zhihu.com"
                              "/question/37787176"}):
    try:
        r = requests.get(url_, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return print('连接异常')


def main():
    url0 = input("请输入合规网址：")

    # 诸如https://www.zhihu.com/api/v4/questions/305888519/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=&limit=&sort_by=default&platform=desktop
    # 诸如https://www.zhihu.com/api/v4/questions/305888519/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%
    # 2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.
    # is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B*%5D.
    # mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&
    # offset=&limit=&sort_by=default&platform=desktop

    html0 = getHTMltext(url0, header1).json()
    page = int(html0['paging']['totals'])
    #获得页码数
    n = 0
    while n <= page:
        try:
            url1 = url0[:-48] +'&offset={}&limit=20&sort_by=default&platform=desktop'.format(n)
            # 获得问题,以便新建文件夹
            html1 = getHTMltext(url1,header1).json()
            questitle = html1['data'][0]['question']['title']
            for datas in html1['data']:
                urlfile = re.findall(r'data-original="(https://.*?)"', datas['content'])
                # 获得网址
                urls = list(set(urlfile))
                # 去除重复的网址
                if urls.__len__() == 0:
                    continue
                    #没有发图片的回答则终止
                for url in urls:
                #保存每一个图片，并命名
                    local_path = url[8:].replace('/', '')[32:]
                    # 取网址的一部分进行命名
                    url = url[:11] + '3' + url[12:]
                    # 带有***pic3***的网址才能爬取，暂不知为何
                    rs = getHTMltext(url)
                    time.sleep(0.1)
                    # 慢慢来别急
                    dir_path = 'E://{}//'.format(questitle)
                    # 用问题作为创建文件夹的名称
                    if not os.path.exists(dir_path):
                        os.mkdir(dir_path)
                        # 判断有无此文件夹，无则创建，有就不管
                    path = dir_path + local_path
                    # 图片地址
                    with open(path, "wb") as f:
                        f.write(rs.content)
                        print("正在保存{}".format(path))
                        # 将图片保存到本地
        except:
            pass
        n +=20
        time.sleep(2)


header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/69.0.3497.100 Safari/537.36', 'Host': 'www.zhihu.com',
                        'Referer': "https://www.zhihu.com/question/37787176"
           }


if __name__ == '__main__':
    main()

