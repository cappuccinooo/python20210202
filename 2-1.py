import random
a = random.randint(1,20)
while True:
    b = int(input('number:'))
    if a == b:
        print('答對')
        break
    else:
        print('答錯')
    
