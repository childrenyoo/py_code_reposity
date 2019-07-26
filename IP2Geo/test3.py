#百度地图api：通过IP查地址
from urllib import request
import json

# ak is bound with ip
baidu_api_ak = "UasTkGnlX3NAKiS675ux8OCIrTP6AFDc"
ip_addr = "202.120.235.200"
# Request url
url = "http://api.map.baidu.com/location/ip?output=json&ak=" + baidu_api_ak + "&ip=" + ip_addr
url1='https://api.map.baidu.com/highacciploc/v1?qcip='+ip_addr+'&qterm=pc&ak='+baidu_api_ak+'&coord=bd09ll'
req = request.Request(url)
res = request.urlopen(req)
res = res.read()
# Bytes to str
n = res.decode(encoding='utf-8')
# str to json
s = json.loads(n)
t = json.dumps(s, ensure_ascii=False)

print(t)