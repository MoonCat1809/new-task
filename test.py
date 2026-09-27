import turtle
import ssetcolor
'''
def code_block():
    while True:
        n=int(input(ssetcolor.bg_black(ssetcolor.black('ddtlbnt xbckj'))))

        h = input(ssetcolor.bg_black(ssetcolor.black('+, -, *, %')))

        b=int(input(ssetcolor.bg_black(ssetcolor.black('ddtlbnt xbckj'))))

        def cacalator():
            if h=='+':
                c = n + b
                return c
            elif h=='-':
                s = n - b
                return s
            elif h=='*':
                r = n * b
                return r
            elif h == '**':
                k = n ** b
                return k
            else:
                t = n / b
                return t

        print(ssetcolor.bg_black(ssetcolor.black(cacalator())))

code_block()
'''
import random
turtle.speed(20)
'''
for g in range(1000):

    x = random.randint(1, 1000)
    y=random.randint(1,1000)
    z = random.randint(1, 1000)

    for b in range(10):
        
        turtle.forward(100)
        turtle.left(x-y/z)
    
'''
def star(n):
    for g in range(1000):
        for b in range(10):

            turtle.forward(100)
            turtle.left(180 - 180 / n)

star(float(input()))








