#ip138查询；精确到区
import requests
from bs4 import BeautifulSoup
ip1 = "202.120.235.200"
ip2="222.72.152.114"
ip3="43.240.129.76"
ip4="183.162.6.218"
url = "http://ip138.com/ips138.asp"
param = {'ip':ip2}
r = requests.request('GET', url, params=param)
r.encoding = 'gbk'
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
soup = soup.ul

print("查询接口1：\n", soup.contents[0].string[5:])
print("查询接口2：\n", soup.contents[1].string[6:])
print("查询接口3：\n", soup.contents[2].string[6:])
