import requests
from bs4 import BeautifulSoup

res = requests.get("https://world.taobao.com/search/search.htm?_ksTS=1495311888184_326&spm=a21bp.7806943.a214x9l.1.haxwFz&_input_charset=utf-8&navigator=all&json=on&q=%E8%BF%9E%E8%A1%A3%E8%A3%99&callback=__jsonp_cb&cna=lZckD8UWxHUCAXL2WWJ2yCq7&abtest=_AB-LR517-LR854-LR895-PR517-PR854-PR895")

soup = BeautifulSoup(res.text, 'html.parser')

for item in soup.select('#list-body'):
    print item