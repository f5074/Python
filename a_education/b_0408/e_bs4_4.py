#coding:euc-kr
import urllib.request

# naver Ȩ���������� �̹��� ��ũ�� ����
url = "https://ssl.pstatic.net/tveta/libs/1173/1173551/cd062c53dbb106a5f2bd_20180115165020097.jpg"

savename ='imagetest1.jpg'# �̹����� ������ ���ϸ� ����

mem = urllib.request.urlopen(url).read()
with open(savename, mode = "wb") as frank:  # wb = write binary
    frank.write(mem)
    print("����Ǿ����ϴ�")