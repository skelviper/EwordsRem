# 用于单词记忆的工具

import os
import sys
import getch

# update on july11 2019
from tqdm import tqdm

# 选择词汇表
os.system('clear')
print("Choose the wordlist:")
print("1.CET-6  2.TOELF  3.GRE")
a = input("input your choice,number only")
os.system('clear')


# 通过空格结束输入而不是回车
def custom_input(prefix=""):
    """Custom string input that submits with space rather than enter"""
    concatenated_string = ""
    sys.stdout.write(prefix)
    sys.stdout.flush()
    while True:
        key = ord(getch.getch())
        # If the key is enter or space
        if key == 32 or key == 13:
            break
        concatenated_string = concatenated_string + chr(key)
        # Print the characters as they're entered
        sys.stdout.write(chr(key))
        sys.stdout.flush()
    return concatenated_string


# 打开文件,如果碰到一个不存在的文件就算了，等着之后创建
count = 0


try:
    with open('wordlist/'+a+'_progress.txt', 'r+') as progress:
        count = int(progress.read())
except:
    pass


# count 是当前到多少单词的一个计数


with open('wordlist/'+a+'_son.txt', 'r', encoding='UTF-8') as wordlist:
    lines = wordlist.readlines()    # 接收数据


# 从上回结束的开始遍历
    for line in lines[count:]:     # 遍历数据

        # 下面是进度条
        pbar = tqdm(lines)
        pbar.update(count)
        pbar.close()

        print("")
        print("")
        print(line)
        print("")

        # 核对输入是否正确，变量num用于表示这一行进行到了第几个字母
        num = 0

        word = custom_input()
        os.system('clear')
        for i in line:
            if line[num] == ' ':
                break
            num += 1
        with open('wordlist/'+a+'_progress.txt', 'w') as progress:
            # 如果不想继续随时exit跑路
            while(word == "exit"):
                progress.write(str(count))
                progress.close()
                os._exit(0)
            while(word != line[0:num]):
                os.system('clear')
                print(line)

                # time.sleep(0.01)
                # p.update(count+1)

                word = custom_input()
                while(word == "exit"):
                    progress.write(str(count))
                    progress.close()
                    os._exit(0)

        count += 1

        os.system('clear')  # 每个单词输入完成后清屏
        # p.finish()
