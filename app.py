#!/user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from sys import path
import os

path.append(os.getcwd() + "\\starvoice")
from starvoice.starvoice import execLoki

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

#with open("line_credit.json","r",encoding="utf-8") as e:
    #line_credit = json.load(e)
#line_creditDICT = dict(line_credit.items())

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def linebot():
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    refDICT = { # value 必須為 list
        #"key": []
    }    
    
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        access_token = os.environ.get("access_token")
        secret = os.environ.get("channel_secret")
        line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINE 收到的訊息類型
        
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            resultDICT = execLoki(str(msg), filterLIST=filterLIST, refDICT=refDICT, splitLIST=splitLIST)   #Loki判斷intent
            if resultDICT != {}:
                reply = resultDICT["response"][0]   #回傳回覆字串
            else:
                reply = "抱歉，我只是個機器人，沒辦法回答喔"   #回傳/沒有答案時的預設回覆字串
        else:
            reply = '你傳的不是文字呦～請再試一次'
            
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))    # 回傳訊息

    except:
        print(body)                                                                   # 如果發生錯誤，印出收到的內容
        reply = '我是預設的回覆字串，目前機器人發生了一些問題，請稍後再試一次!'            # 如果發生錯誤，預設的回覆訊息
                
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()