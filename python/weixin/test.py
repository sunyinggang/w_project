import requests








def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


def crawl():
    url = "https://mp.weixin.qq.com/mp/profile_ext?" \
    "action=home&" \
    "__biz=MzU5NDgyMjc0OQ==&uin=MjA2NTk4NTM4&" \
    "key=978c9123ca5bf7130d95e84ffce01334af033b41e75e2db3c87765187267e34bd0e930038fd322fa7441d9413aa3ab5b1b253c377eac679be62cacc959c" \
    "34ca021e73fbd68887e512f67244b9a4a0cfd&devicetype=Windows+10&ver" \
    "sion=62080079&lang=zh_CN&a8scene=7&pass_ticket=R5VEsP%2F5J4D%2FRH" \
    "S382NGFNIp2mSePFluS7QsX6VHK1M%3D&winzoom=1"

    headers = """
Host: mp.weixin.qq.com
Cookie: wxuin=206598538; devicetype=Windows10; version=62080079; lang=zh_CN; pass_ticket=/SSknx152esFNBtXf2hJtJqJKftyHbps7SxqRWVqxjo=; wap_sid2=CIrjwWISXEpJY0pfekw1dUxrY3FUN21zNDJmNUF4ejNOU0QxcnF0bEoxaHNfM2lGYjYtUGk2ekVsSEtKV0VsN09wbUhIdC1QekVDQVBtTXdxbHZkdzZUMXlrNU5pUUVBQUF+MIbq3/UFOA1AlU4=
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)

if __name__ == '__main__':
    crawl()

