#!/user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from sys import path
import os
from datetime import datetime
import logging

from reserve_bot import execLoki as reserve_loki
from starvoice import execLoki as qa_loki

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
@app.route("/", methods=['POST'])

def linebot():
    body = request.get_data(as_text=True)                # 取得收到的訊息內容
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
        
        # ############## message handling ############### 
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            
            if msg.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                reply = msg + "\n" + "我是陽明交大星聲社機器人\你可以用我來問問題或預約團室\n請問您今天想問什麼呢?"
                
            filterLIST = []
            splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
            refDICT = {}
            
            if msg.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                reply = msg + "\n" + "我是陽明交大星聲社機器人\你可以用我來問問題或預約團室\n請問您今天想問什麼呢?"
                
            elif msg.lower() in ["掰掰","掰","88","bye bye","bye","再見", "沒有", "拜拜"]:
                reply = "掰掰，謝謝您的使用，期待下次為您服務!"
                
            else:
                try:
                    resultDICT = reserve_loki(str(msg), filterLIST=[], refDICT=refDICT, splitLIST=splitLIST)   #Loki語意判斷是否為預約intent
                    print("loki complete")
                    print(resultDICT)
                    
                    if resultDICT != {}:
                        if resultDICT["time"] == None:                        
                            reply = "請輸入你要預約的時段!\n例如: 星期五晚上8點到10點"
                        else:
                            reply = "了解，你要預約「{}」的{}".format(resultDICT["time"][0], resultDICT["location"][0])            #回傳回覆字串
                            
                    else:
                        resultDICT = qa_loki(str(msg), filterLIST=filterLIST, refDICT=refDICT, splitLIST=splitLIST)   #Loki語意判斷是否為QA intent
                        if resultDICT != {}:                        
                            reply = resultDICT["response"][0]            #回傳回覆字串
                        else:
                            reply = "抱歉，我只是個機器人，沒辦法回答喔"    #回傳/沒有答案時的預設回覆字串
                            
                except:
                    reply = "抱歉發生一些問題~請再試一次"   #非文字訊息回覆
                        
        else:
            reply = '不是文字，我可是不吃的喔~請再試一次'   #非文字訊息回覆
            
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply)) # 回傳訊息
            
            
    except Exception as e:
        print("[ERROR] => {}".format(str(e)))
        print(body)                                                                   # 如果發生錯誤，印出收到的內容
    
    await(reply)                                                             
    return 'OK'                                                                       # 驗證 Webhook 使用，不能省略   

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)