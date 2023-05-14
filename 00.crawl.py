from urllib.request import urlopen
from bs4 import BeautifulSoup

# 특정 사이트 호출
html = urlopen("http://www.tcpschool.com/")

# BeautifulSoup() = Python과 함께 쓰이는 Parser.
bsObject = BeautifulSoup(html, "html.parser")

# 뉴스 내용을 호출하기위해 <a> 태그의 src 속성을 호출해옴
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('src'))