#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for classes

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_classes.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[classes] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "吉他社課是什麼時候":
        if CHATBOT_MODE:
            if args[3] == None:
                resultDICT["response"] = getResponse("有社課嗎", args)
            else:
                args[3] = args[3].replace(" ", "").lower()
                if args[3] in ["鼓", "爵士鼓"]:
                    resultDICT["response"] = getResponse("鼓社課是什麼時候", args)
                elif args[3] in ["pa"]:
                    resultDICT["response"] = getResponse("PA社課是什麼時候", args)                
                elif args[3] in ["貝斯", "bass"]:
                    resultDICT["response"] = getResponse("貝斯社課是什麼時候", args)
                elif args[3] in ["kb", "keyboard"]:
                    resultDICT["response"] = getResponse("KB社課是什麼時候", args)
                elif args[3] in ["主唱", "vocal"]:
                    resultDICT["response"] = getResponse("主唱社課是什麼時候", args)
                elif args[3] in ["吉他", "結他"]:
                    resultDICT["response"] = getResponse("吉他社課是什麼時候", args)
                else:
                    resultDICT["response"] = "抱歉，我們沒有{}社課喔!".format(args[3])
        else:
            pass

    if utterance == "有什麼社課":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "吉他社課是星期一":
        if CHATBOT_MODE:
            if args[2] == None:
                resultDICT["response"] = getResponse("有社課嗎", args)
            else:
                args[2] = args[2].replace(" ", "").lower()
                if args[2] in ["鼓", "爵士鼓"]:
                    resultDICT["response"] = getResponse("鼓社課是什麼時候", args)
                elif args[2] in ["pa"]:
                    resultDICT["response"] = getResponse("PA社課是什麼時候", args)                
                elif args[2] in ["貝斯", "bass"]:
                    resultDICT["response"] = getResponse("貝斯社課是什麼時候", args)
                elif args[2] in ["kb", "keyboard"]:
                    resultDICT["response"] = getResponse("KB社課是什麼時候", args)
                elif args[2] in ["主唱", "vocal"]:
                    resultDICT["response"] = getResponse("主唱社課是什麼時候", args)
                elif args[2] in ["吉他", "結他"]:
                    resultDICT["response"] = getResponse("吉他社課是什麼時候", args)
                else:
                    resultDICT["response"] = "抱歉，我們沒有{}社課喔!".format(args[2])
        else:
            pass
        
    if utterance == "社課都辦在什麼時候":
        if CHATBOT_MODE:
            if args[3] == None:
                resultDICT["response"] = getResponse("有社課嗎", args)
            else:
                args[3] = args[3].replace(" ", "").lower()
                if args[3] in ["鼓", "爵士鼓"]:
                    resultDICT["response"] = getResponse("鼓社課是什麼時候", args)
                elif args[3] in ["pa"]:
                    resultDICT["response"] = getResponse("PA社課是什麼時候", args)                
                elif args[3] in ["貝斯", "bass"]:
                    resultDICT["response"] = getResponse("貝斯社課是什麼時候", args)
                elif args[3] in ["kb", "keyboard"]:
                    resultDICT["response"] = getResponse("KB社課是什麼時候", args)
                elif args[3] in ["主唱", "vocal"]:
                    resultDICT["response"] = getResponse("主唱社課是什麼時候", args)
                elif args[3] in ["吉他", "結他"]:
                    resultDICT["response"] = getResponse("吉他社課是什麼時候", args)
                else:
                    resultDICT["response"] = "抱歉，我們沒有{}社課喔!".format(args[3])
        else:
            pass

    if utterance == "有社課嗎":
        if CHATBOT_MODE:
            args[5] = args[5].replace(" ", "").lower()
            if args[5] == None or args[5] in ["鼓", "爵士鼓", "pa", "貝斯", "bass", "kb", "keyboard", "主唱", "vocal", "吉他", "結他"]:    
                resultDICT["response"] = getResponse(utterance, args)
            else:
                resultDICT["response"] = "抱歉，我們沒有{}社課喔!".format(args[5])
        else:
            pass
        
    if utterance == "有沒有社課":
        if CHATBOT_MODE:
            if args[3] == None:
                resultDICT["response"] = getResponse("有社課嗎", args)
            else:
                args[3] = args[3].replace(" ", "").lower()
                if args[3] in ["鼓", "爵士鼓"]:
                    resultDICT["response"] = getResponse("鼓社課是什麼時候", args)
                elif args[3] in ["pa"]:
                    resultDICT["response"] = getResponse("PA社課是什麼時候", args)                
                elif args[3] in ["貝斯", "bass"]:
                    resultDICT["response"] = getResponse("貝斯社課是什麼時候", args)
                elif args[3] in ["kb", "keyboard"]:
                    resultDICT["response"] = getResponse("KB社課是什麼時候", args)
                elif args[3] in ["主唱", "vocal"]:
                    resultDICT["response"] = getResponse("主唱社課是什麼時候", args)
                elif args[3] in ["吉他", "結他"]:
                    resultDICT["response"] = getResponse("吉他社課是什麼時候", args)
                else:
                    resultDICT["response"] = "抱歉，我們沒有{}社課喔!".format(args[3])
        else:
            pass

    return resultDICT