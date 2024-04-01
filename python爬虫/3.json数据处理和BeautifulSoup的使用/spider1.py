import requests,json


def main():
    url = "http://api.help.bj.cn/apis/weather2d/?id=扬州"
    resp = requests.get(url=url)
    content = resp.content.decode('utf-8')
    # 把字符串变成了字典
    data = json.loads(content)
    # 访问json转化后的字典
    print(data['tomorrow']['temp'])
    pass


if __name__ == '__main__':
    main()
