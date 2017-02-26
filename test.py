# -*- coding: utf-8 -*-
#!/usr/bin/python
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.shanbay.com/team/thread/188584/1920688/')
page = pq(response.content)
innerpage = page('div#post-10859098')
innerpage =innerpage('div.post-content-todo.well')
innerpage =innerpage('div.post-content-todo')
print innerpage('h1 strong').text()
