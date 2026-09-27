import random
import ssetcolor as st

while True:
    k = input(st.blue('камень, ножницы, бумага\n'))
    wintable = [
        ["камень", "камень", "draw"],
        ["камень", "ножницы", "unwin"],
        ["камень", "бумага", "win"],
    ]


    def Ai():
        n = ['камень', 'ножницы', 'бумага']
        a = random.choice(n)
        return a


    if k == 'камень' and Ai() == 'ножницы':
        print(st.yellow('You is win'))

    elif k == 'камень' and Ai() == 'бумага':
        print(st.red('You is unwin'))

    elif k == 'камень' and Ai() == 'камень':
        print(st.bg_black('Draw'))

    elif k == 'бумага' and Ai() == 'камень':
        print(st.yellow('You is win'))

    elif k == 'бумага' and Ai() == 'ножницы':
        print(st.red('You is unwin'))

    elif k == 'бумага' and Ai() == 'бумага':
        print(st.bg_black('Draw'))

    elif k == 'ножницы' and Ai() == 'бумага':
        print(st.yellow('You is win'))

    elif k == 'ножницы' and Ai() == 'камень':
        print(st.red('You is unwin'))

    else:
        print(st.bg_black('Draw'))








