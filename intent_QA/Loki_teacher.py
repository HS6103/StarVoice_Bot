#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for teacher

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

DEBUG = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_teacher.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[teacher] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[星聲社]的指導[老師]是誰":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] == '老師':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社]的指導[老師][背景]":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] == '老師' and args[2] in ['背景', '資歷']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[是]否有指導[老師]":
        if CHATBOT_MODE:
            if args[1] == '老師':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[你們]的指導[老師]是誰":
        if CHATBOT_MODE:
            if args[0] in ['你們', '我們', ''] and args[1] == '老師':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass


    return resultDICT