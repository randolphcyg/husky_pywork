'''
@Author: randolph
@Date: 2020-06-11 21:29:42
@LastEditors: randolph
@LastEditTime: 2020-06-11 22:17:11
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import random


def guess_num():
    user = int(input("猜一猜随机生成的整数为多少："))
    computer = random.randint(1, 50)        # 整数范围1-50，可以修改
    i = 1
    while True:
        if user < computer and user != 0:
            user = int(input("不好意思，猜小了！"))
            i += 1
        elif user > computer and user != 0:
            user = int(input("不好意思，猜大了！"))
            i += 1
        elif user == computer:
            print("恭喜你，猜对了")
            print("游戏结束！")
            exit()
        if i == 10:
            print("很遗憾，下次加油")
            exit()


if __name__ == "__main__":
    guess_num()
