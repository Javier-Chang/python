import requests
import json
from bs4 import BeautifulSoup

LOGIN_URL = 'http://hsin.tillandsia.com.tw/ddftest/login.php'
LOGIN_URL2 = 'http://hsin.tillandsia.com.tw/ddftest/buy.php'

def main():
        s = requests.session()
        s.get(LOGIN_URL)
        phpssid = s.cookies['PHPSESSID']
        #print (phpssid)

        payload = {
            'username': 'def',
            'pass':''
        }

        header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'26',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'PHPSESSID='+phpssid,
        'Host':'hsin.tillandsia.com.tw',
        'Origin':'http://hsin.tillandsia.com.tw',
        'Referer':LOGIN_URL,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        header2 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'26',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'PHPSESSID='+phpssid,
        'Host':'hsin.tillandsia.com.tw',
        'Origin':'http://hsin.tillandsia.com.tw',
        'Referer':LOGIN_URL2,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        
        result = s.post(LOGIN_URL, data = payload, headers = header)
        #print(result)
        #print (result.encoding)
        result.encoding = 'utf-8'
        soup = BeautifulSoup(result.text, 'html.parser')
        #print(soup)
        a_tags = soup.find('a', href="buy.php")
        # for tag in a_tags:
        #     # 輸出超連結的文字
        #     print(tag.string) 
        #print ('coin 拍幣： ' + str(a_tags.string))


        result2 = s.post(LOGIN_URL2, data = payload, headers = header2)
        result2.encoding = 'utf-8'
        soup2 = BeautifulSoup(result2.text, 'html.parser')
        #print(soup2)

        option_list = soup2.find_all('option')
        #print(option_list)

        for option in option_list:
            print ('value: {}, text: {}'.format(option['value'], option.text))




if __name__ == '__main__':
    main()
