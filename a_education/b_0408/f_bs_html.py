#coding:euc-kr
from bs4 import BeautifulSoup
html ="""
<html><body>
<h1>����� ȣ����</h1>
<p>ȣ���� ������ �а����ΰ�?</p>
<p>�泲�� ���帶ũ - õ�Ⱦƻ꿪���� 5�аŸ�</p>
</body></html>
"""
# �Ľ��� ���ؼ� �� �ٷ� ������ �ҽ��� ���� ���� �Ѵ�.
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print("h1 = " + h1.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)

