import requests
from bs4 import  BeautifulSoup
import pandas as pd


def get_page_content(requests_url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
    html=requests.get(requests_url,headers=headers,timeout=10)
    content=html.text
    soup=BeautifulSoup(content,'html.parser')
    return soup
def analysis(soup):
    df=pd.DataFrame(columns=['id','brand','car_model','type','desc','problem','datetime','status'])
    temp=soup.find('div',class_='tslb_b')
    tr_list=temp.find_all('tr')
    for tr in tr_list:
        td_list=tr.find_all('td')
        if len(td_list)>0:
            id,brand,car_model,type,desc,problem,datetime,status=\
                td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,\
                td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            # print(id,brand,car_model,type,desc,problem,datatime,status)
            temp={}
            temp['id']=id
            temp['brand']=brand
            temp['car_model']=car_model
            temp['type']=type
            temp['desc']=desc
            temp['problem']=problem
            temp['datatime']=datetime
            temp['status']=status
            df=df.append(temp,ignore_index=True)
    return df

result=pd.DataFrame(columns=['id','brand','car_model','type','desc','problem','datetime','status'])
base_url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num=20
for i in range(page_num):
    requests_url=base_url+str(i+1)+'.shtml'
    soup=get_page_content(requests_url)
    df=analysis(soup)
    result=result.append(df)
print(result)
result.to_csv('car_complaindata',index=False)