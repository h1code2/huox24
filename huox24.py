import requests
import execjs
import json

with open("huox.js", "r", encoding="utf-8") as file:
    js_code = file.read()

ctx = execjs.compile(js_code)

sign = ctx.call("v")

headers = {
    'sec-fetch-mode': 'cors',
    # 'cookie': '_ga=GA1.2.1039764404.1568709768; _gid=GA1.2.1485176288.1568709768; USD=6.833898; Hm_lvt_d70f8822d1ff168453d5ea7b3e359297=1568709768,1568709888; Hm_lpvt_d70f8822d1ff168453d5ea7b3e359297=1568709888; SERVERID=29dcb2c2e0682adea06ad95c2d4fe0cc|1568710043|1568709766',
    'dnt': '1',
    'sign-param': sign,
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://www.huoxing24.com/',
    'authority': 'www.huoxing24.com',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-site': 'same-origin',
}

params = (
    ('currentPage', '1'),
    ('pageSize', '10'),
    ('deviceSource', 'web'),
)

response = requests.get('https://www.huoxing24.com/info/lives/showlives', headers=headers, params=params)

print(json.dumps(response.json(), indent=4, ensure_ascii=False))

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.huoxing24.com/info/lives/showlives?currentPage=1&pageSize=10&deviceSource=web', headers=headers)
