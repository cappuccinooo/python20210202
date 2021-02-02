c=0
import random
a = random.randint(1,20)
while True:
    b = int(input('number:'))
    if a > b:
        print('太小了!')
        c=c+1
    if c >= 5:
        print('遊戲結束!')
        break
    elif a < b:
        print('太大了!')
        c=c+1
    elif a == b:
        print('答對了!')
        c=c+1
        print(c,'次')
        break

        
    