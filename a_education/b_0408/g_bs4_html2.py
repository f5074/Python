#coding:euc-kr
from bs4 import BeautifulSoup
html ="""
<html><body>
<div id = "food">
    <h1> �ʹ��� �԰� ���� �� </h1>
    <ul class = "items">
        <li> �����ʹ�</li> 
        <li> �����ʹ�</li>
        <li> ���� ��ù�</li>
    </ul>
</div>
</body></html>
"""
# ���� �κ� �����ϱ�
soup = BeautifulSoup(html,'html.parser')
# �ϳ��� ���� div id =food �ȿ� h1�� �����´�.
h1= soup.select_one("div#food > h1")
print( "h1 =" ,h1.string) # string�� ���ڸ� ���� �س���.
# ��� �κ� ����
# ul class = items�ȿ� li�� ��� �����´�.
li_list = soup.select("div#food > ul.items > li" )
for li in li_list:
    print("li = ", li.string) # string = ���ڸ� �����´�.