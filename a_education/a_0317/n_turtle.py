#coding: euc-kr
import turtle # ��Ʋ �׷��� ����� �ҷ��´�.
import random # ���� ����� �ҷ��´�.

screen = turtle.Screen()
image1 = "C:\\Users\\cpc-001\\PycharmProjects\\test0317\\images\\rabbit.GIF"
image2 = "C:\\Users\\cpc-001\\PycharmProjects\\test0317\\turtle.GIF"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle() # ù ��° �ź��̸� �����Ѵ�.
t1.shape(image1)
t1.pensize(5) # ���� �β��� 5�� �Ѵ�.
t1.penup() # ���� ���.
t1.goto(-300, 0) # (-300, 0) ��ġ�� ����.

t2 = turtle.Turtle() # �� ��° �ź��̸� �����Ѵ�.
t2.shape(image2)
t2.pensize(5) # ���� �β��� 5�� �Ѵ�.
t2.penup() # ���� ���.
t2.goto(-300, -200) # (-300, -100) ��ġ�� ����.

t1.pendown() # ù ��° �ź����� ���� ������.
t2.pendown() # ù ��° �ź����� ���� ������.
t1.speed(1)
t2.speed(1)

for i in range(100): # 100�� �ݺ��Ѵ�.
	d1 = random.randint(1, 60) # 1���� 60 ������ ������ .
	t1.forward(d1) # ������ŭ .
	d2 = random.randint(1, 60) # 1���� 60 ������ ������ .
	t2.forward(d2)