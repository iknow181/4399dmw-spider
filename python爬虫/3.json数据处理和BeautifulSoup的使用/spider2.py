# 加载json数据
from pprint import pprint
import requests,json

url = "http://192.168.92.129/test/a.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Referrer": "www.baidu.com"
}
resp = requests.get(url,headers=headers)
# print(resp.content.decode('utf-8'))
# 美化打印
pprint(json.loads(resp.content))