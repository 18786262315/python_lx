import requests
from htmlparsing import Element, HTMLParsing, Text, Attr, Parse

url = 'http://localhost:8082/home/serveList.html'
r = requests.get(url)
article_detail = HTMLParsing(r.text).detail({'title': Text('a.storylink'),
                                             'points': Parse('span.score', '>{} points'),
                                             'link': Attr('a.storylink', 'href')})
print(article_detail)