from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://kb.or.kr/p/?j=18/"
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다.

soup = BeautifulSoup(source, "html5lib") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
table = soup.find(class_="pad5 lh_140")
movies = table.find_all(class_="lpad15")

for movie in movies:
    title = movie.get_text()
    print(title, end=' ')
    link = movie.a.get('href')
    url = 'https://www.rottentomatoes.com' + link
    print(url)