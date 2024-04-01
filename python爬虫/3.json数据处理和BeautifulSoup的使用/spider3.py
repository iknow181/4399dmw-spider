# 保存和读取


import requests, json

url = "http://192.168.92.129/test/a.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Referrer": "www.baidu.com"
}
resp = requests.get(url, headers=headers)
# 保存一下
with open('a.txt', 'w', encoding='utf-8') as f:
    # ensure_ascii=False可以显示中文，indent=2把子节点向后移动2个空格
    json.dump(resp, f, ensure_ascii=False, indent=2)

# 读取本地json文件
with open('a.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
