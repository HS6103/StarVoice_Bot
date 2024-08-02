#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for misc

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_misc.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[misc] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[星聲社][logo]設計[想法]是什麼":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1].lower.strip(' ') in ['logo', '商標', '圖案'] and args[2] == '想法':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社][厲害]嗎":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] in ['厲害', '強']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社][是]否有與[產業界]合作":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and ('業' or '公司' in args[2]) :
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社]對[學校]有哪些貢獻":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] in ['學校']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社]是[熱音社]嗎":
        if CHATBOT_MODE:
            if args[0] == '星聲社':
                if args[1] == '熱音社':
                    resultDICT["response"] = getResponse(utterance, args)
                elif '社' in args[1]:
                    resultDICT["response"] = '星聲社不是{}喔，我們是交大的熱音社'.format(args[1])
        else:
            pass

    if utterance == "[星聲社]有[社團][logo]嗎":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[2].lower.strip(' ') in ['logo', '商標', '圖案']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社]的[英文]翻譯":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] in ['英文', '英語', '美語']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[星聲社]與哪些[產業界]合作":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and ('產業' or '公司' in args[1]) :
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "參加[星聲社]對[職涯]發展有幫助嗎":
        if CHATBOT_MODE:
            if args[0] == '星聲社' and args[1] in ['職業', '職涯']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT