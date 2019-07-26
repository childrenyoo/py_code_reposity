# coding=utf-8
# 百度地图api：通过经纬度查地址
from urllib import request
import json


baidu_api_ak = "UasTkGnlX3NAKiS675ux8OCIrTP6AFDc"
url = "http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=31.0449,121.4012&output=json&pois=1&ak=" + baidu_api_ak
req = request.Request(url)
res = request.urlopen(req)
res = res.read()
n = res.decode(encoding='utf-8')
n = n[len("renderReverse&&renderReverse") + 1:-1]
st = json.loads(n)
result = st["result"]
for i in result:
    print(i, result[i])