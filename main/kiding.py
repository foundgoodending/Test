import random

number = random.choice(range(100))
temp = -1
while number != temp:
    temp = int(input('请输入数字'))
    print("")
    if temp > number:
        print('猜大了')
    elif temp < number:
        print('猜小了')
    elif temp == number:
        print('猜对了')