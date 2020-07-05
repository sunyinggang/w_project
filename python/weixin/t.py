import requests


def crawl():
    # url中的参数需要根据自己的情况做调整
    url = "https://mp.weixin.qq.com/mp/profile_ext?" \
          "action=home&" \
          "__biz=MjM5MzgyODQxMQ==&" \
          "scene=124&" \
          "devicetype=iOS10.3.3&" \
          "version=16060022&" \
          "lang=zh_CN&nettype=WIFI&a8scene=3&" \
          "fontScale=100&" \
          "pass_ticket=CSprpmr8jgRyCI4Y%2FW9Er99kmPVPzaKYXOTD140oDqj%2Bs%2F69p7m09jaVxogugn%2BX&" \
          "wx_header=1"

    headers = """
Host: mp.weixin.qq.com
Cookie: wxuin=206598538; devicetype=Windows10; version=62080079; lang=zh_CN; pass_ticket=/SSknx152esFNBtXf2hJtJqJKftyHbps7SxqRWVqxjo=; wap_sid2=CIrjwWISXEpJY0pfekw1dUxrY3FUN21zNDJmNUF4ejNOU0QxcnF0bEoxaHNfM2lGYjYtUGk2ekVsSEtKV0VsN09wbUhIdC1QekVDQVBtTXdxbHZkdzZUMXlrNU5pUUVBQUF+MIbq3/UFOA1AlU4=
X-WECHAT-KEY: 54320db02e367ad058a5c9cfdd9e4bf780c10666163fd5b8b030b1220c07f79c5775dfb1690eeea1f8f5b13c47ce09aacbd5c564f6c712d48af72c5bf015fd0dc326a0d734b8792b518ce9297fcb0540
X-WECHAT-UIN: ODQxNTI1NzYw
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
Connection: keep-alive
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    if '<title>验证</title>' in response.text:
        raise Exception("获取微信公众号文章失败，可能是因为你的请求参数有误，请重新获取")
    data = extract_data(response.text)
    for item in data:
        print(item)


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles


def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


if __name__ == '__main__':
    crawl()