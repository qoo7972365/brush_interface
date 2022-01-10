import requests,json,os
import urllib3
import time
import random
from concurrent.futures import ThreadPoolExecutor
import datetime
import re
from urllib.parse import quote
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def create_user():
    get_csrf_cookies = {
        '_csrf_token': '47f53d5a93beff1aa4ef0753716a48579b9f5bb0dd766f1d3195fcdd72f64ae3',
        'PHPSESSID': '0nojre5l3nonta0mi5escadhrk',
        'my-application-browser-tab': '',
        'AWSALB': 'IGH94uKrN7w5yEVS9uoP97fceyhQOmTCNxtvRtHb1Ng1pJinhHZvD86OVVD4RTt4Ob1okBM5/eKcQfnZ7OHyMXazmggAt1oE+cJCqSoZKTXTdkoKkmnnrHsRt+DX',
    }
    
    get_csrf_headers = {
        'X-Forwarded-For': '192.168.0.91',
        'X-Originating-IP': '192.168.0.92',
        'X-Remote-IP': '192.168.0.93',
        'X-Remote-Addr': '192.168.0.94',
        'X-Client-IP': '192.168.0.95',
        'Host': 'www.1542727.com',
        'Sec-Ch-Ua': '"Chromium";v="95", ";Not A Brand";v="99"',
        'Accept': 'text/html, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.1542727.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    #response = requests.get('https://www.1542727.com/login/registerTab', headers=get_csrf_headers, cookies=get_csrf_cookies, verify=False)
    ## print(response.text)
    #if response.status_code == 400:
    #    print('請求街口異常')
    #elif response.status_code == 504:
    #    print('服務器異常')
    #elif response.status_code == 403:
    #    print('遭地區限制')
    #elif response.status_code == 200:
    #    response = response.text
    #    # response = json.loads(response)
    #    pattern = r'rf_cs_rForm_.*'
    #    first_str = re.findall(pattern, response)[0]
    #    csrf = first_str[23:-4]
    #    csrf_encode = quote(csrf, 'utf-8')

    cookies = {
        '_csrf_token': 'cf7638812854d578dd6f03c6f4999f65bdff573c6fde9584ed9e424e542acc90',
        'AWSALB': 'p08ovf3gODQj2li2a99eQLRwcAEN/mI/SkBdib8p9zT6FrPXx1Bc9ZVWZf77d3TRdJinObyQL0wIwmMAqzQ8X/GH8qRhgP3SGNS2W1VRVGiXPl3DTh6MS9AFua9k',
        'AWSALBCORS': 'p08ovf3gODQj2li2a99eQLRwcAEN/mI/SkBdib8p9zT6FrPXx1Bc9ZVWZf77d3TRdJinObyQL0wIwmMAqzQ8X/GH8qRhgP3SGNS2W1VRVGiXPl3DTh6MS9AFua9k',
        'PHPSESSID': '68qhsbek9lst3ouq3aq56h788c',
        'my-application-browser-tab': '',
    }

    headers = {
        'Host': 'www.1542727.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '281',
        'Origin': 'https://www.1542727.com',
        'Connection': 'close',
        'Referer': 'https://www.1542727.com/',
    }
    csrf_token = "e08fb2efaa1464b4b07a8ca458665fa4eRIn3NayygvZdyt9PsohBDJDuCCk7Rhc0SICEOQN16j0w2mBNKGhTrXn7R5qPfXsFlttpsTh9f34OxSetwGXzg%3D%3D"
    username = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789',10))
    data = 'username={0}&password=fdgfdgfd&referral_code=&captcha=3960&cg_bind=0&cg_account_id=&cg_bind_from=register&rf_cs_rForm_={1}&password_confirmation=fdgfdgfd'.format(username,csrf_token)

    response = requests.post('https://www.1542727.com/login/registerUser', headers=headers, cookies=cookies, data=data, verify=False)
    now = datetime.datetime.now()
    if  response.status_code == 400 :
        print('請求接口異常')
        os.system("echo {1}   {0} 請求接口異常 >> /tmp/123.txt".format(response.status_code, now))

    elif  response.status_code == 504 :
        print('服務器異常')
        os.system("echo {1}   {0} 服務器異常 >> /tmp/123.txt".format(response.status_code, now))
    elif  response.status_code == 403 :
        print('遭地區限制')
        os.system("echo {1}   {0} 遭地區限制 >> /tmp/123.txt".format(response.status_code, now))
    elif response.status_code == 200:
        response = response.text
        response = json.loads(response)
        message = response['message']
        code = response['code']
        ###账户已被使用，请重新输入
        if code == "EA008":
            pass
        else:
            print(message,username)
            account_list.append(username)
            os.system("echo {1}   200 {0}帳號創建成功 >> /tmp/123.txt".format(username,now))
    else:
        os.system("echo {1}   {0} 請求失敗,其他異常 >> /tmp/123.txt".format(response.status_code, now))
        print(response.status_code)
        print(response.text)

        
account_list = []
def run(total_time,processes):
    with ThreadPoolExecutor(max_workers=processes) as executor:
        future_tasks = {executor.submit(create_user(),count,): count for count in range(total_time)}


start = time.time()
total_time = 10000000
processes = 10
run(total_time,processes)
end = time.time()
#print('開始時間',start)
#print('結束時間',end)
print('運行時間',int(end - start),"線程數",processes,"刷接口數量",total_time,"帳號數量",len(account_list))

#if __name__ == "__main__":
#    start = time.time()
#    number = 0
#    for number in range(1,100):
#        create_user(number)
#    end = time.time()
#    print('開始時間',start)
#    print('結束時間',end)
