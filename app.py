from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

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



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if re.match('沫兒',event.message.text):
        MoReply = True #沫兒確認匹配成功
    message = TextSendMessage(text='沫兒收到您的回覆囉!')
    # message = TextSendMessage(text=event.message.text)
    if MoReply == True:
        line_bot_api.reply_message(event.reply_token, message)
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
