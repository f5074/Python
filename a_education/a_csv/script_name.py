#coding:euc-kr
import sys # ���̽㿡 �⺻������ ����Ǿ� �ִ� sys ����� �ҷ��´�. �� ����� ��� �ٿ��� 
             # �߰������� �Էµ� �μ��� ��ũ��Ʈ�� �Ѱ��ش�.

input_file = sys.argv[1] # sys ����� argv��� �μ��� ����ϴµ�, �� �μ��� ����� ���� ��
output_file = sys.argv[2] # �߰������� �ԷµǴ� �μ��� ����Ʈ �ڷ������� �޴´�.


with open(input_file, 'r', newline='') as filereader: # ���� ��ü�� �����ָ�,    
 # open() �Լ����� ��r'�� �б� ��带 �Ҵ��Ѵ�. �̴� input_file�� �б� ���� �������� �ǹ��Ѵ�.
   with open(output_file, 'w', newline='') as filewriter: # ���� ��ü�� �����ָ�,
      # ��w'�� ���� ��带 �Ҵ��ϰ� output_file�� ���� ���� �������� �ǹ��Ѵ�.
      # ����, with ���� with ���� ����� �� �ڵ����� ���� ��ü�� �ݴ´�. 
      header = filereader.readline() # readline() �Լ��� ����Ͽ� �Է� ������ ù ��° 
             # ��(��� ��)�� ���ڿ��� �а� �̸� header��� ������ �Ҵ��Ѵ�.
      header = header.strip() # strip() �Լ��� ����Ͽ� header�� �ִ� ���ڿ��� �糡���� 
                        # ����, �� �� ���๮��(\n) ���� ������ �� header�� �ٽ� �Ҵ��Ѵ�.
      header_list = header.split(',') # split() �Լ��� ����Ͽ� ���ڿ��� ��ǥ ����
                 # ���� �����Ͽ� ����Ʈ�� �Ҵ��ϸ�, ����Ʈ�� �� ���Ҵ� �Է� ������ �� ���� 
                 # ����̸�, header_LIST��� ������ �Ҵ�ȴ�.
      print(header_list) # HEADER_LIST�� ��(��, ��� ��)�� ȭ�鿡 ����Ѵ�.
      filewriter.write(','.join(map(str,header_list))+'\n') # write() �Լ��� 
           # ����Ͽ� header_list�� �� ���� ��� ���Ͽ� ����. map() �Լ��� header_list�� �� 
           # ���ҿ� str() �Լ��� �����Ͽ� �����Ҹ� ���ڿ��� ����� join() �Լ��� header_list�� 
           # �� �� ���̿� ��ǥ�� �����ϰ� ����Ʈ ���ڿ��� ��ȯ�Ѵ�. �� ���� ���� ���ڸ� ���ڿ� 
           # ���� �߰��ϸ�, filewriter ��ü�� �� ���ڿ��� ��� ������ ù ��° �࿡ ����Ѵ�.
      for row in filereader: # for ���� ����Ͽ� �Է� ������ ������ ���� �ݺ��Ѵ�.
          row = row.strip()
          row_list = row.split(',')
          print(row_list)
          filewriter.write(','.join(map(str,row_list))+'\n')