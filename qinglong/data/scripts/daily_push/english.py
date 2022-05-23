# -*- coding: utf-8 -*-
"""
Author: Lumen
Date: 2022-04-17 10:43:41
LastEditTime: 2022-04-17 12:55:39
LastEditors: Lumen
Description:
👻👻👻👻👻👻👻👻
"""
import sys

sys.path.append("../")
import requests
import json
import wechat_push

# 企业微信
CID = "ww5d2407f0c86d0105"
AID = "1000002"
SECRET = "OQO8xP94ySbd-Hpk3ElSZHPa72Nfs-9lVJb2omu1Pig"

# 天行数据api接口key
APIKEY = "7d34b3e4f303527a3fc769c0fefd0c16"


def get_cated_users_list() -> str:
    string = ""
    with open("push_name.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for p in data["PeopleList"]:
        string += p + "|"

    return string[:-1]


def get_random_VanEnglishSentence(APIKEY: str):
    base_url = "http://api.tianapi.com/everyday/index?key="
    url = base_url + APIKEY
    r = requests.get(url)
    if r.status_code == 200:
        return json.loads(r.text)["newslist"][0]
    else:
        return None


def push_content_to_users():
    push = wechat_push.WechatPush(corp_id=CID, secret=SECRET, agent_id=AID)
    get_dict = get_random_VanEnglishSentence(APIKEY)
    # 拼接内容
    content = f'{get_dict["content"]}\n{get_dict["note"]}'
    cated_users_list = get_cated_users_list()
    push.send_text(content, cated_users_list)


if __name__ == "__main__":
    push_content_to_users()
