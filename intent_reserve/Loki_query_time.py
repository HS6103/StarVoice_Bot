#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for query_time

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os
import datetime
from ArticutAPI import Articut

DEBUG = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_query_time.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[query_time] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def argToDatetime(arg=""):
    try:
        with open("account.info", encoding="utf-8") as f:
            accountDICT = json.load(f)
            username = accountDICT['username']
            api_key = accountDICT['api_key']
            
    except Exception:
        username = os.environ.get('loki_username')
        api_key = os.environ.get('articut_key')
    
    try:
        articut = Articut(username=username, apikey=api_key)    
        resultDICT = articut.parse(arg, level='lv3', timeRef=str(datetime.datetime.now())[0:19])    # 取得 resultDICT
        
        datetimeArg = datetime.datetime(                                                            # 把 resultDICT 的時間變成 datetime
            resultDICT["time"][0][0]["time_span"]["year"][0],
            resultDICT["time"][0][0]["time_span"]["month"][0],
            resultDICT["time"][0][0]["time_span"]["day"][0],
            resultDICT["time"][0][0]["time_span"]["hour"][0],
            resultDICT["time"][0][0]["time_span"]["minute"][0],
            resultDICT["time"][0][0]["time_span"]["second"][0],
        )
        
    except Exception:
        datetimeArg = None
        
    return datetimeArg
    
def getCorrectTime(timeLIST):
    """
    Calculates correct start/end time

    Input:
        timeLIST          list
        
    Output:
        timeResultDICT    dict
        
    """
    datetimeLIST = []
    for time in timeLIST:
        if time == None:
            datetimeLIST.append(None)
        else:
            datetimeLIST.append(argToDatetime(time))
            
        
    # 將結果放入 timeResultDICT
    timeResultDICT = {
        "start": datetimeLIST[0], 
        "end": datetimeLIST[1]
    }
    
    return timeResultDICT


def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[7].":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}點'.format(args[0]), None])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True
            
    if utterance == "[7點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime([args[0], None])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True
            
    if utterance == "[7]:[00]~[9]:[00]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}點{}分'.format(args[0], args[1]), '{}點{}分'.format(args[2], args[3])])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    if utterance == "[7]:[00]到[9]:[00]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}點{}分'.format(args[0], args[1]), '{}點{}分'.format(args[2], args[3])])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True
            
    if utterance == "[8].~[10].":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}點'.format(args[0]), '{}點'.format(args[1])])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    if utterance == "[早上][8].~[10].":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}{}點'.format(args[0], args[1]), '{}點'.format(args[0], args[3])])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    if utterance == "[晚上][7].":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}{}點'.format(args[0], args[1]), None])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    if utterance == "[晚上][7].到[9].":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime(['{}{}點'.format(args[0], args[1]), '{}點'.format(args[0], args[3])])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    if utterance == "[晚上七點]到[九點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            timeResultDICT = getCorrectTime([args[0], args[1]])
            resultDICT['start'] = timeResultDICT['start']
            resultDICT['end'] = timeResultDICT['end']
            resultDICT["time"] = True

    return resultDICT