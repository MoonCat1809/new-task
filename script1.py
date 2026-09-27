import random
import ssetcolor as st

n = random.randint(-100, 100)
u = input(st.yellow('Вы хотите пользовательский или игру с ИИ '))
if u == 'пользовательский':
    h = int(input(st.black('Введите число для угадывания ')))
    for i in range(100):
        print(st.bg_black('...---...'))
        while True:
            a = int(input('Введите предположительное число'))
            if a > h:
                print(st.white('Надо меньше!!!!'))

            elif a < h:
                print(st.red('Надо больше!!!!'))

            else:
                print(st.yellow('Угадал!!!!;)'))
                break

else:
    while True:
        a = int(input(('Введите предположительное число')))
        if a > n:
            print(st.white('Надо меньше!!!!'))

        elif a < n:
            print(st.red('Надо больше!!!!'))

        else:
            print(st.yellow('Угадал!!!!;)'))
            break