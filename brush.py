import requests,json
import urllib3
import time
import random
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def create_user():
    cookies = {
        '_csrf_token': '4f1b388d7ca0a2bfca1eba8e23149cc5c18e9d12854fb7aebb4cc97cefb1f86e',
        'PHPSESSID': '0nojre5l3nonta0mi5escadhrk',
        'my-application-browser-tab': '',
        'AWSALB': 'SqjCpoUnnoRLXHZj3+bsyVHJA6STF1NkXdQNWmRE4szQRaXxj56OhFjZfuuHqGOXzTxmnPxUHl9SBqlNHMLAzJ8fbsmgseZ9mHQPBggj1SanRSRXgR6Ttvl8xQBX',
    }
    
    headers = {
        'Host': 'www.1542727.com',
        'Content-Length': '277',
        'Sec-Ch-Ua': '"Chromium";v="95", ";Not A Brand";v="99"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Origin': 'https://www.1542727.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.1542727.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    username = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789',10))
    #data = 'username={0}&password=fdgfdgfdg&referral_code=&captcha=4777&cg_bind=0&cg_account_id=&cg_bind_from=register&rf_cs_rForm_=2BB3cm5zsTTAN3dWrx8U3SmKQvaEm2tvAHXJdieYlOvUwO7HpNA%3D%3D&password_confirmation=fdgfdgfdg'.format(username)
    data = 'username={0}&password=fdgfdgfd&referral_code=&captcha=7934&cg_bind=0&cg_account_id=&cg_bind_from=register&rf_cs_rForm_=bae2de263ddef313489f8b1635f10d93wQfV3OaAoB9LBpr2v6CqWlJ3VjdBCdVbtgwfHD0MYB61X788x6Abf%2B376MbsKuhBxyJvYKM807vpb7%2B%2FG1pqZQ%3D%3D&password_confirmation=fdgfdgfd'.format(username)

    response = requests.post('https://www.1542727.com/login/registerUser', headers=headers, cookies=cookies, data=data, verify=False)
    if  response.status_code == 400 :
        print('請求街口異常')

    elif  response.status_code == 403 :
        print('遭地區限制')
    else:
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

account_list = []
def run(total_time,processes):
    with ThreadPoolExecutor(max_workers=processes) as executor:
        future_tasks = {executor.submit(create_user(),count,): count for count in range(total_time)}


start = time.time()
total_time = 1000000
processes = 1
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
