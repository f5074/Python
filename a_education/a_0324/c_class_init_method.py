#coding:euc-kr
class Car:
    def __init__(self):
        self.drive()
    def drive(self):
        self.speed = 60

myCar = Car()
# myCar.speed = 0
myCar.color = "blue"
myCar.model = "E-Class"
myCar.year = "2017"


# print(myCar.speed)


print("�ڵ��� ��ü ����")
print("�ڵ��� �ӵ� : ",myCar.speed)
print("�ڵ��� ���� : ",myCar.color)

print("�ڵ��� �� : ",myCar.model)
myCar.drive()
print("�ڵ��� �ӵ� : ",myCar.speed)

