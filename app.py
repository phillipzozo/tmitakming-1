import threading
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from linebot.exceptions import LineBotApiError

import os
app = Flask(__name__)


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import time
import datetime
import schedule
#時間偏移+8hour
a = datetime.datetime.today()
o = datetime.timedelta(hours=8)
#print((a+o).strftime("%Y-%m-%d_%H:%M"))
# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
db = firestore.client()

#首次上傳時初始化用
path_root = "Detector"
collection_ref = db.collection(path_root)
docs = collection_ref.get()
cc = 0
for doc in docs:
    #print("文件內容：{}".format(doc.to_dict()))
    cc += 1  # 取得最後一筆流水號
#print(cc)
#path = "Detector/gas"+str(cc) #現版本被禁用 暫時忽略
#doc_ref = db.document(path)
temp = ''
doc_ref = db.collection('Detector').document('gas')


def query_resetSearch():
    path_root = "Detector"
    collection_ref = db.collection(path_root)
    docs = collection_ref.get()
    cc = 0
    for docx in docs:
        #print("文件內容：{}".format(doc.to_dict()))
        cc += 1  # 取得最後一筆流水號
    #print(cc)
    #path = "Detector/gas"+str(cc)
    #doc_ref = db.document(path)
    path = "gas"+str(cc)
    return db.collection('Detector').document(path)


def query_Get():
    # 初始化firestore
    doc_ref = query_resetSearch()
    #Get Collection
    global temp
    temp = ''
    try:
        doc = doc_ref.get()
        # 透過 to_dict()將文件轉為dictionary
        temp += 'id => {}'.format(doc.to_dict()['id']) + '\n' + 'PM2.5 => {}'.format(doc.to_dict()['PM2.5']) + '\n' + '二氧化碳 => {}'.format(doc.to_dict()['CO2']) + '\n' + '酒精 => {}'.format(doc.to_dict()['Ethanol']) + '\n' + '一氧化碳 => {}'.format(
            doc.to_dict()['CO']) + '\n' + '溫度 => {}'.format(doc.to_dict()['temperture']) + '\n' + '濕度 => {}'.format(doc.to_dict()['humidity']) + '\n' + '時間戳 => {}'.format(doc.to_dict()['timestamp']) + '\n'
        # print("文件內容為：{}".format(doc.to_dict()))
        #print(temp)
       # print(doc_ref)
      #  print(doc)
    except:
        temp = '發生意外錯誤'
       # print(temp)


def queryInsert(insertStr):
    query_resetSearch()
    tempstr = 'gas'+str(cc)
    doc_ref = db.collection("Detector").document(tempstr)
    doc_ref.set(insertStr)

#try:
 #   doc = doc_ref.get()
    # 透過 to_dict()將文件轉為dictionary
 #   print("文件內容為：{}".format(doc.to_dict()))
#except:
  #  print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))


test = []
cc += 1  # 下一個流水號

test = {'id': cc, 'CO2': 1100, 'Ethanol': 0.4, 'CO': 200, 'PM2.5': 299,
        'temperture': 30, 'humidity': 50, 'timestamp': (a+o).strftime("%Y-%m-%d %H:%M:%S")}
#queryInsert(test)
#query_Get()




# Channel Access Token
line_bot_api = LineBotApi( 'MIgVrNiPJz5nNBDgMYE7/pmAl8fR2kue2oyLonZowuDtFVC2LNe/U0LNJ73GolHxMVfv2g0uj5pQJcNZOPKwOSJ7rQ133IeKj3Cn2ZGYJ6HG6Yb3OkmtSgfdI0fomqs7YoqOILlBcYy53AXWLxixcAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8c54ffae7c41efd0d30013d1e13f7a1a')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#字串匹配 用來是否呼叫沫兒的
import re
MoReply = False  #沫兒未確認匹配不回覆訊息

to = "U59f95fe4a4acf87b3433b626f41679b8" #userID 推播用


def job():
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)
  #  if int((a+o).strftime("%M")) == 0:
  #  line_bot_api.push_message('Cd28e03928239ba4bfb9ba96f758861d4', TextSendMessage(
  #      text="報時~ 現在時間："+(a+o).strftime("%Y-%m-%d %H:%M:%S")))
    line_bot_api.push_message('C18d381b48c034f3de0af914fe1fe524f', TextSendMessage(text="報時~ 現在時間："+(a+o).strftime("%Y-%m-%d %H:%M:%S")))
    timer = threading.Timer(60, job)
    timer.start()




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

      
    if re.match('沫兒',event.message.text):
        MoReply = True #沫兒確認匹配成功
    message = TextSendMessage(text='沫兒收到您的回覆囉!')
    if re.search('我帥嗎',event.message.text):
        message = TextSendMessage(text='沫兒覺得勝舢最帥了!')
    if re.search('回報車內狀況',event.message.text):
        query_Get()
        message = TextSendMessage(text=temp)
    if re.search('新增資料',event.message.text):
        queryInsert(test)
        message = TextSendMessage(text='新增成功') #未來加入感測器失效錯誤回報
    # message = TextSendMessage(text=event.message.text)
    if re.search('profile_user',event.message.text):
        user_id = event.source.user_id
        message = TextSendMessage(text=user_id)
    if re.search('profile_group', event.message.text):
        group_id = event.source.group_id
        message = TextSendMessage(text=group_id)
    if re.search('profile_room', event.message.text):
        room_id = event.source.room_id
        message = TextSendMessage(text=room_id)
    if re.search('測試推播',event.message.text):
        job()
        line_bot_api.push_message('C18d381b48c034f3de0af914fe1fe524f', TextSendMessage(text=(a+o).strftime("%Y-%m-%d %H:%M:%S")))
  
    if MoReply == True:
        line_bot_api.reply_message(event.reply_token, message)
    

#傳圖測試
#圖片訊息
# ImageSendMessage物件中的輸入
# original_content_url 以及 preview_image_url都要寫才不會報錯。
#輸入的網址要是一個圖片，應該說只能是一個圖片，不然不會報錯但是傳過去是灰色不能用的圖
image_url = "https://192.192.140.141/web/2.jpg"
try:
    line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
except LineBotApiError as e:
    # error handle
    raise e








if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    timer = threading.Timer(60, job)
    timer.start()
   
