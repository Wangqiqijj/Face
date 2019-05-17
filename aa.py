# -*- coding: utf-8 -*-
from aip import AipFace
import base64
import json
import sys

APP_ID = '16247626'
API_KEY = '7GDbn7b19ngp8hLGlK9KBTBy'
SECRET_KEY = 'AsZA0szX9VkojRgfOfHU8sLfmo3nwu42'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
 

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath = "./qw.jpg"
with open(filePath,"rb") as f:  
# b64encode是编码
	base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

groupIdList = "77"

""" 调用人脸搜索 """
a = client.search(image, imageType, groupIdList);
#name=a['result']['user_list'][0]['user_id']
#score=a['result']['user_list'][0]['score']
print(a)
print(type(a['result']))
print(str(a['result']))
print(type(type(a['result'])))
