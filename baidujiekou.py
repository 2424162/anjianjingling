import urllib.request
import sys
import base64
import json
import os
url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=7bKwmfkP3sGBLHkDtzS3GY0c&client_secret=SvujTnuu4nAgw8Pwdu98qtLKZsN3HISO'
print("__")

def get_photo(path):
    with open(path,'rb') as f:
        return base64.b64encode(f.read())
def response(url):
    request= urllib.request.Request(url)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response=urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    jsons=json.loads(content)
    js=jsons["access_token"]
    print(js)
    return js
def tupianji():
       list=[]
       dir="C:\\Users\Lenovo\Desktop\图片\\"
       for rt,dirs,files in os.walk(dir):
           for filename in files:
               filename=dir+filename
               list.append(filename)
       return list



def ceshi(img,token):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token="

    url2=url+token
    imgs= {"image": img}
    imgs = urllib.parse.urlencode(imgs).encode('utf-8')
    request = urllib.request.Request(url2, data=imgs)
    request.add_header('Content-Type','application/x-www-form-urlencoded')
    try:
     response = urllib.request.urlopen(request)
     content = response.read()
     print(content.decode())
     return content.decode()
    except:
        pass
token=response(url)
filename=tupianji()
#data = open('C:\\Users\Lenovo\Desktop\\quanguodata12.txt','w+')

for file in filename:
    print(file)
    photo=get_photo(file)
    line = ceshi(photo,token)
   # try:
   #  data.write(line+'\n')
   # except:
    #    pass

