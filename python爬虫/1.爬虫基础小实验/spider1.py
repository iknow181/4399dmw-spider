import requests


def main():
    url = "https://www.4399dmw.com/search/dh-0-0-0-0-1-{}-0/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }

    for i in range(2):
        urla = url.format(i)
        print(urla)
        resp = requests.get(url=urla, headers=headers)
        with open("a" + str(i) + ".txt", "wb+") as f:
            # 写入文件
            f.write(resp.content)
    pass


if __name__ == '__main__':
    main()
