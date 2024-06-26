import urllib.request, json
from urllib.request import Request, urlopen

req = Request(
    url='https://api.gurufocus.com/public/user/50e22a65250e1766d8807bf4b5326447:92ec970347a4143ea9d377fe833dd658/stock/MATX/keyratios',
    headers={'User-Agent': 'Mozilla/5.0'}
)
content = urlopen(req).read()
data = json.loads(content.decode('utf8'))
print(data)
print(data['Valuation Ratio']['PE Ratio'])
print(data['Basic'])
