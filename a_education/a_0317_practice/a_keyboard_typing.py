# coding:euc-kr

import random
import time

print("="*40)
print("Ÿ�� ����")
print("="*40)
start = time.time()
ex = ["������","�����","������","ȣ����","����","�ڻԼ�","�⸰","ǥ��","�ڳ���", "�罿","��","�ϸ�"]
cnt = 1
while True:
      ex2 = random.choice(ex)
      print("����.({})".format(cnt))
      print(ex2)
      ex_answer = input()

      if ex2 == ex_answer:
         print("���")
         cnt += 1
      else:
         print("����...��õ�!")
      if cnt == 6:
         end = time.time()
         res = end - start
         print("�� �ð��� {0}�� �Դϴ�.".format(res))
         break