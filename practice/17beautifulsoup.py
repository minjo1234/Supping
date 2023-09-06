from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# 참고사이트
soup = BeautifulSoup(html_doc, 'html.parser')

# 삼성전자접근 soup = BeautifulSOup(html, 'html.parser')
# html.parser을 이용해서 삼성전자에 접근한다.

print(soup.prettify())
print('🙂🙂🙂')
print()

print(soup.title)  # title 전체
print(soup.title.string)  # title 태그의 문자열
print(soup.title.parent.name)  # title 태그의 부구

print(soup.p)
print(soup.p['class'])
print()

print(soup.a)
print(soup.find_all('a'))
print()
print(soup.find(id='link3'))
