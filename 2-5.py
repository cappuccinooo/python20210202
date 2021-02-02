import turtle,time

b = turtle.Turtle()

a = turtle.Turtle()

aa = int(input('要畫幾邊形'))
aaa = 70

aaaa = 360.0/ aa

for i in range(aa):
    a.forward(aaa)
    b.forward(aaa)
    b.left(aaaa)
    a.right(aaaa)
    time.sleep(1)
    
turtle.dome()

    