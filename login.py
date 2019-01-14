import requests
import json
from bs4 import BeautifulSoup

user_id = '1234556778888'
user_pw = '1234556778888'
LOGIN_URL = 'http://localhost/connect.php'
URL = 'http://127.0.0.1/member.php/'

def main():
        s = requests.session()

        s.get(LOGIN_URL)
        #所有的cookie值皆存在cookies中
        #print (s.cookies)
        #PHPSESSID存在s.cookies的PHPSESSID欄位中
        phpssid = s.cookies['PHPSESSID']
        #print (phpssid)
        payload = {
            'id': user_id,
            'pw': user_pw,
            'button': '登入'
        }

        header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'39',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':phpssid,
        'Host':'127.0.0.1',
        'Origin':'http://127.0.0.1',
        'Referer':LOGIN_URL,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        
        result = s.post(LOGIN_URL, data = payload, headers = header)
        print(result)
        soup = BeautifulSoup(result.text, 'html.parser')
        print(soup)


if __name__ == '__main__':
    main()
