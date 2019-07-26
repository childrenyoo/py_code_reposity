import requests
from faker import Faker

f = Faker('zh-CN')
ip1 = "202.120.235.200"
ip2="222.72.152.114"
ip3="47.52.27.159"
ip4="183.162.6.218"
res1 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=202.120.235.200')
# res2 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=222.72.152.114')
# res3 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=47.52.27.159')
# res4 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=183.162.6.218')

def printaddr(ip,r):
    if r.json()['code'] == 0:
        i = r.json()['data']
        country = i['country']  # 国家
        area = i['area']  # 区域
        region = i['region']  # 地区
        city = i['city']  # 城市
        isp = i['isp']  # 运营商
        print("IP:",ip)
        print(u'国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, area, region, city, isp))
    else:
        print("ERROR! ip: %s" % ip)

printaddr(ip1,res1)
# printaddr(ip2,res2)
# printaddr(ip3,res3)
# printaddr(ip4,res4)