import requests
import re
import json
import time

# url ='https://www.zhihu.com/api/v4/questions/39369539/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=8&platform=desktop&sort_by=def'
# kv = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

def gethtml(url):
    try:
        kv = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

        r = requests.get(url,headers = kv)
        r.raise_for_status
        r.encoding= r.apparent_encoding
        return r.text
    except:
        print('解析失败')


def printlist(html):
    json_data =json.loads(html)

    for datas in json_data['data']:
        r_title = datas['question']['title']
       
        print(r_title)
        print('***'*20)

        r_text1=re.findall(r'[\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+',datas['content'])
    #正则表达式只能提取中文及中文符号，不能提前数字，字母
        for r_text2 in r_text1:
            print(r_text2)
        print('***'*20)
        return r_title





def main():
    url1 ='https://www.zhihu.com/api/v4/questions/39369539/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=25&platform=desktop&sort_by=default'
                        
    urls=[url1[:-42]+'offset={}&platform=desktop&sort_by=default'.format(i) for i in range(0,200,5)]
    for url in urls:
        html = gethtml(url)
        
        printlist(html)
        
main()











    

