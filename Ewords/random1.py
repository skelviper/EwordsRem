import random

lines=open(a+ '.txt').readlines()
new = []  # 定义一个空列表，用来存储结果
for line in lines:
    temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
    temp2 = temp1.split(',')  # 以','为标志，将每行分割成列表
    new.append(temp2)  # 将上一步得到的列表添加到new中
random.shuffle(new)#乱序一个列表
#print(new)
fm=open(a + '_son.txt', 'w')
for i in new:
    x=len(i)
    for j in i[0:x-1]:
        fm.write(j)
        fm.write(',')
    for j in i[x-1]:
        fm.write(j)#去除列表中最后一个逗号
    fm.write("\n")
fm.close()
