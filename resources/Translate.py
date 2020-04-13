from flask_restful import Resource, reqparse
import requests
import json

class  Translate(Resource):

    def post(self,text):

         url='https://translate.yandex.net/api/v1.5/tr.json/translate'
         api_key= 'trnsl.1.1.20200412T164420Z.b8899d0058b1565d.42dff98dbe0cb561ecf8c9bb0f2a905decab97ce'
         params=dict(key=api_key, text=text, lang='en-es')
         res=requests.get(url,params=params)
         y=res.json()
         return y["text"]



#     url='https://translate.yandex.net/api/v1.5/tr.json/translate'
#
#
#     res=requests.get(url)
#
#     api_key= 'trnsl.1.1.20200412T164420Z.b8899d0058b1565d.42dff98dbe0cb561ecf8c9bb0f2a905decab97ce'
#
# #    params=dict(key= api_key, text="Hello", lang='en-ru')
#     params=dict(key= api_key, text=text, lang=en-es)
#
#     res=requests.get(url,params=params)
#
#     print(res.text)
