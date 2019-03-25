#用于单词记忆的工具
#skelviper 3/16/2019

import os
import random
import progressbar
import time

#选择词汇表
print("Choose the wordlist:")
print("1.CET-6  2.TOELF  3.GRE")
a = input("input your choice,number only")


#打开文件,如果碰到一个不存在的文件就算了，等着之后创建
count=0
try:   
    with open('wordlist/'+a+'_progress.txt', 'r+') as progress:
        count = int(progress.read())
except:
    pass


#count 是当前到多少单词的一个计数





with open('wordlist/'+a+'_son.txt', 'r', encoding='UTF-8') as wordlist:
    lines = wordlist.readlines()    # 接收数据

    p = progressbar.ProgressBar()
    N = len(lines)
    p.start(N)

#从上回结束的开始遍历
    for line in lines[count:]:     # 遍历数据
        print(line)
        
        #核对输入是否正确，变量num用于表示这一行进行到了第几个字母
        num = 0
        
        word = input()
        for i in line:
                if line[num] == ' ':
                    break
                num += 1
        with open('wordlist/'+a+'_progress.txt','w') as progress:
            #如果不想继续随时exit跑路
            while(word == "exit"):
                progress.write(str(count))
                progress.close()
                os._exit(0)
            while(word != line[0:num]):
                os.system('clear')
                print(line)
                
                #time.sleep(0.01)
                p.update(count+1)
                
                word = input()
                while(word == "exit"):
                    progress.write(str(count))
                    progress.close()
                    os._exit(0)
        count += 1
            

        os.system('clear') #每个单词输入完成后清屏
        #p.finish()