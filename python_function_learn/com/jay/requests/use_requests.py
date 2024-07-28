import requests

r = requests.get('https://www.douban.com/')  # 豆瓣首页
print(r.status_code)

# print(r.text)

r = requests.get('https://www.douban.com/search', params={
    'q': 'python', 'cat': '1001'})
print(r.url)

print(r.encoding)

# get 请求
r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

# post 请求
r = requests.post('https://accounts.douban.com/login', data=
{'form_email': 'abc@qq.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 如果要传递JSON数据，可以直接传入json参数：
url = 'https://accounts.douban.com/login'
params = {'key': 'value'}
r = requests.post(url, json=params)

# 上传文件
upload_file = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_file)

