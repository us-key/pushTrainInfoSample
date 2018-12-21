import requests
import json

def request(nameArr):
    url = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
    response = requests.get(
        url,
    ).json()
    flg = False
    print(response)
    for name in nameArr:
        for dic in response:
            if dic['name'] == name:
                msg = name + 'の遅延情報があります。'
                flg = True
    if not flg:
        msg = '遅延情報はありません'
    return msg
