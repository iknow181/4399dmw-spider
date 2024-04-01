import requests
from retrying import retry


# 如果失败就请求3次，执行3次如果还失败就报错，可以配合try
@retry(stop_max_attempt_number=3)
def qingqiou(inurl):
    url = inurl
    print('start request')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }
    res = requests.get(url, headers=headers)
    with open("a.txt", "wb+") as f:
        f.write(res.content)
    print("request seccuss")


def main():
    try:
        qingqiou("https://www.4399dmw.com/search/dh-0-0-0-0-1-2-0/")
    except:
        print("requset fail")
    pass


if __name__ == '__main__':
    main()
