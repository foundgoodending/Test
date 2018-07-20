for num in range(1,100):
    for temp in range(2,num):
        if num % temp == 0:
            break
    else:
            print(num,'是质数')