#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for future

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_future.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[future] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[星聲社][未來]希望達成的[目標]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[星聲社][未來]有什麼計畫或[目標]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[星聲社][未來]有哪些[計畫]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[星聲社][未來]的[規劃]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[星聲社]的[未來]發展[方面]是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[星聲社]的[長遠]發展":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    return resultDICT