import requests
from concurrent.futures import ThreadPoolExecutor

def creatr_acc(count):
    cookies = {
        'ASP.NET_SessionId': 'ieqyz33dcepg24bcq0w4wu1j',
    }

    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Origin': 'http://vn99.vip',
        'Referer': 'http://vn99.vip/Index/login',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
    }

    params = (
        ('ApiInterface', 'gonggao'),
    )

    response = requests.post('http://vn99.vip/api/NotLoggedInApi', headers=headers, params=params, cookies=cookies, verify=False)
    print(count,response.json()['statusCode'])


def run():
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_tasks = {executor.submit(creatr_acc,count): count for count in range(1000000)}
run()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://vn99.vip/api/NotLoggedInApi?ApiInterface=gonggao', headers=headers, cookies=cookies, verify=False)
