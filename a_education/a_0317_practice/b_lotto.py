#coding:euc-kr


import random

print("="*50)
print("�ζ� ��ȣ")
print("="*50)

while True:
      put_money = int(input("�ݾ��� �Է��Ͻÿ�. : "))
      print("\n")
      game_cnt = put_money // 1000
      if put_money % 1000 == 0:

          for i in range(game_cnt):
              lotto = random.sample(range(1,46),6) # �ζǶ�� ������ 1~45
                                               # ���� �� 6���� ���Ƿ� ����
              lotto.sort() # �������� ����Ǵ� ���� ����
              print("{0:>2} GAME : {1}".format(i+1,lotto))
              if (i+1) == 5:
                  print("="*50)
      else:
          print("1000�� ������ �Է��ϼ���. : ")
          print("\n")
      if put_money == 0:
         break