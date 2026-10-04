import tkinter
import random
import ssetcolor as st
import time
import string

while True:
    p=['1-Змейка',
       '2-Игра больше/меньше',
       '3-Калькулятор',
       '4-Игра камень/ножницы/бумага',
       '5-Игра сапер',
       '6-Скоропечатанье']
    print(st.blue(p))
    n=input(st.blue('Введите число выбора?'))
    if n == '1':

        window = tkinter.Tk()
        window.title('Snake')
        window.geometry('900x900')
        window['bg'] = 'white'

        can = tkinter.Canvas(window, width=900, height=900, bg='#CCC19A')
        can.pack()

        rectangle = 20

        Right_go = 'Right'

        snake = [(100, 100), (80, 100), (60, 100)]
        apple = []
        food = {"normal": {"color": "#E2252B", "score": 1},
                "gold": {"color": "#FFCF40", "score": 2},
                "poison": {"color": "#00FF00", "score": -1},
                "texno": {"color": "white", "score": 0},
                "speed": {"color": "#FF6700", "score": 2},
                "slow": {"color": "#64C6E3", "score": 1}, }
        speed = 300
        balli = 0
        speed_original = 300
        speed_timer = None

        balle = tkinter.Label(window, text='Счёт: 0', bg='white', fg='#a7b309', font=('Times', 20))
        balle.pack()


        def go_snake():
            can.delete('snake')
            for segment in snake:
                x, y = segment
                can.create_rectangle(x, y, x + rectangle, y + rectangle, fill='#a2b37a', tag='snake')


        def food_apple():
            global apple
            apple.clear()
            can.delete('apple')
            two_tip = ['normal', random_vibor()]
            for food_type in two_tip:
                while True:
                    x = random.randint(0, 23) * rectangle
                    y = random.randint(0, 23) * rectangle
                    if (x, y) not in snake and (x, y) not in [a[:2] for a in apple]:
                        apple.append((x, y, food_type))
                        break
                color = food[food_type]['color']
                can.create_oval(x, y, x + rectangle, y + rectangle, fill=color, tag='apple')


        def random_vibor():
            cgayns = random.randint(1, 100)
            if cgayns <= 2:
                return 'texno'
            elif cgayns <= 5:
                return 'gold'
            elif cgayns <= 15:
                return 'poison'
            elif cgayns <= 35:
                return 'speed'
            elif cgayns <= 45:
                return 'slow'
            else:
                return 'normal'


        def go_go():
            global apple, speed, balli, speed_timer

            if not snake:
                return

            head_x, head_y = snake[0]
            if Right_go == 'Right':
                now_head = (head_x + rectangle, head_y)
            elif Right_go == 'Left':
                now_head = (head_x - rectangle, head_y)
            elif Right_go == 'Up':
                now_head = (head_x, head_y - rectangle)
            elif Right_go == 'Down':
                now_head = (head_x, head_y + rectangle)

            if (
                    now_head in snake or
                    now_head[0] < 0 or now_head[0] >= 900 or
                    now_head[1] < 0 or now_head[1] >= 900
            ):
                can.create_text(400, 400, text='Пфьу щмук нажмите R чтоб переиграть', fill='#a7b309',
                                font=('Times', 20))
                snake.clear()
                return

            snake.insert(0, now_head)
            found_food = None
            for f in apple:
                if now_head[0] == f[0] and now_head[1] == f[1]:
                    found_food = f
                    break

            if found_food:
                fool = found_food[2]
                apple.clear()
                can.delete('apple')
                food_apple()
                if fool == 'normal':
                    balli += 1
                elif fool == 'gold':
                    balli += 2
                elif fool == 'poison':
                    balli += 1
                    if len(snake) > 1:
                        snake.pop()
                elif fool == 'speed':
                    balli += 1
                    speed = max(20, speed - 30)
                    if speed_timer:
                        window.after_cancel(speed_timer)
                    speed_timer = window.after(5000, reset_speed)
                elif fool == 'slow':
                    balli += 1
                    speed = min(300, speed + 30)
                    if speed_timer:
                        window.after_cancel(speed_timer)
                    speed_timer = window.after(5000, reset_speed)
                elif fool == 'texno':
                    balli += 0
                    reset_snake()

                balle['text'] = f'Счёт: {balli}'
            else:
                snake.pop()

            go_snake()
            window.after(speed, go_go)


        def reset_speed():
            global speed
            speed = speed_original


        def reset_snake():
            global snake, Right_go
            Right_go = 'Right'
            snake = [(100, 100), (80, 100), (60, 100)]


        def upravlenie(event):
            global Right_go
            snake_go = event.keysym
            storani = {'Right': 'Left', 'Left': 'Right', 'Up': 'Down', 'Down': 'Up'}
            if snake_go in ['Right', 'Left', 'Up', 'Down'] and snake_go != storani.get(Right_go):
                Right_go = snake_go
            if snake_go == 'r':
                restart_game()


        def restart_game():
            global Right_go, snake, speed, balli, apple
            can.delete('all')
            Right_go = 'Right'

            snake = [(100, 100), (80, 100), (60, 100)]
            speed = 300
            balli = 0
            apple = []

            balle['text'] = 'Счёт: 0'

            go_snake()
            food_apple()
            go_go()


        window.bind('<KeyPress>', upravlenie)

        go_snake()
        food_apple()
        go_go()
        window.mainloop()

    elif n == '2':
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
    elif n == '3':
        while True:
            n = int(input(st.blue('Введите число')))

            h = input(st.yellow('+, -, *, %, **, ='))

            b = int(input(st.blue('Введите число')))


            def cacalator():
                if h == '+':
                    c = n + b
                    return c
                elif h == '-':
                    s = n - b
                    return s
                elif h == '*':
                    r = n * b
                    return r
                elif h == '**':
                    k = n ** b
                    return k
                elif h == '%':
                    t = n / b
                    return t
                elif h == '=':
                    z = n == b
                    return z

                else:
                    j = (st.red('Что не то'))
                    return j


            print(st.underline(cacalator()))
    elif n == '4':
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

    elif n == '5':
        level = 1

        while True:
            size = 5 + level
            if size % 2 == 0:
                size += 1
            player_x = 0
            player_y = 0
            lives = 8
            walls = []

            trea_x = random.randint(0, size - 1)
            trea_y = random.randint(0, size - 1)

            traps = []
            trap_c = level + 2

            type_traps = [
                'obichnai',
                'potion',
                'teleport'

            ]

            for i in range(trap_c):
                while True:
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - 1)

                    bad = False

                    if [x, y] in traps:
                        bad = True

                    if x == 0 and y == 0:
                        bad = True

                    for t in traps:
                        if x == t[0] and y == t[1]:
                            bad = True
                            break

                    if not bad:
                        break

                t = random.choice(type_traps)
                traps.append([x, y, t])

            medkits = []
            medkits_c = max(1, level // 2)

            for i in range(medkits_c):
                while True:
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - 1)

                    bad = False

                    if [x, y] in walls:
                        bad = True

                    if x == 0 and y == 0:
                        bad = True

                    if [x, y] in medkits:
                        bad = True

                    for tr in traps:
                        if x == tr[0] and y == tr[1]:
                            bad = True
                            break

                    if not bad:
                        break

                medkits.append([x, y])

            for y in range(size):
                for x in range(size):
                    if x % 2 == 0 and y % 2 == 0:
                        walls.append([x, y])

            for i in range(size * 2):
                x = random.randint(1, size - 2)
                y = random.randint(1, size - 2)

                if [x, y] in walls:
                    walls.remove([x, y])

            if [0, 0] in walls:
                walls.remove([0, 0])

            while True:
                bad = False

                if trea_x == 0 and trea_y == 0:
                    bad = True

                if [trea_x, trea_y] in walls:
                    bad = True

                if [trea_x, trea_y] in medkits:
                    bad = True

                for trap in traps:
                    if trea_x == trap[0] and trea_y == trap[1]:
                        bad = True
                        break

                if bad:
                    trea_x = random.randint(0, size - 1)
                    trea_y = random.randint(0, size - 1)

                else:
                    break

            rev_traps = []

            print('Игра поймай сокровища')
            print('Найди  сокровище')

            while True:

                print('\n Карта')
                for y in range(size):
                    for x in range(size):
                        if x == player_x and y == player_y:
                            print('X', end=' ')

                        elif [x, y] in medkits:
                            print('M', end=' ')

                        elif [x, y] in rev_traps:
                            print('#', end=' ')

                        elif [x, y] in walls:
                            print(',', end=' ')

                        else:
                            print('.', end=' ')

                    print()

                print('\n Твоя позиция :', player_x, player_y)
                print('Жизни:', lives)

                move = input('Куда идти?')

                old_x = player_x
                old_y = player_y

                if move == 'w' and player_y > 0:
                    player_y -= 1

                elif move == 's' and player_y < size - 1:
                    player_y += 1

                elif move == 'd' and player_x < size - 1:
                    player_x += 1

                elif move == 'a' and player_x > 0:
                    player_x -= 1

                else:
                    print('Нельзя туда идти !!;(')

                if [player_x, player_y] in walls:
                    print('Стоп стена!;>')
                    player_x = old_x
                    player_y = old_y

                if player_x == trea_x and player_y == trea_y:
                    print('\n Ты нашел сокровище!!!;)')
                    level += 1
                    break

                for trap in traps:
                    if player_x == trap[0] and player_y == trap[1]:
                        type_traps = trap[2]
                        rev_traps.append([trap[0], trap[1]])
                        if type_traps == 'obichnai':
                            print('Ты попал в обычную ловушку!:|')
                            lives -= 1
                        elif type_traps == 'potion':
                            print('Ты попал в ловушку с ядом!:[')
                            lives -= 2
                        elif type_traps == 'teleport':
                            print('Ты попал в телепортирующую ловушку!:(')
                            player_x = 0
                            player_y = 0

                        traps.remove(trap)

                        break

                for med in medkits:
                    if player_x == med[0] and player_y == med[1]:
                        print('Ты нашел аптечку!!:)')
                        lives += 1

                        medkits.remove(med)

                        break

                if lives <= 0:
                    print('У вас закончились жизни!')
    elif n=='6':
        width, heght = 900, 700
        sp_speed = 2400
        fal_speed = 5
        comdo = 0
        score = 0
        lives = 5
        level = 1

        start_time = time.time()
        c_letters = 0
        m_letters = 0

        win = tkinter.Tk()
        win.title('Vzlomshik_3000')

        can = tkinter.Canvas(win, width=width, height=heght, bg='#0a0a0a')
        can.pack()

        info = can.create_text(10, 10, text='Очки:0, Жизни:3, Уровень:1', fill='#ff2400', font=('Courier New', 20),
                               anchor='nw')

        go_text = can.create_text(width // 2, 10, text='', fill='#808080', font=('Courier New', 16))

        letters = []


        def update_level():
            global level, fal_speed, sp_speed, start_time, m_letters

            if level == 1 and c_letters >= 15:
                level = 2
                start_time = time.time()
                m_letters = 0

            elif level == 2 and time.time() - start_time >= 30:
                level = 3
                m_letters = 0

            elif level == 3 and c_letters >= 40:
                level = 4
                start_time = time.time()
                m_letters = 0

            if level == 1:
                sp_speed = 2400
                fal_speed = 5

            elif level == 2:
                sp_speed = 1850
                fal_speed = 10

            elif level == 3:
                sp_speed = 1450
                fal_speed = 13
            else:
                sp_speed = 450
                fal_speed = 15


        def spawn_letter():
            x = random.randint(20, width - 20)

            if level == 1:
                tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                                      weights=[60, 20, 10, 2, 8])[0]
            elif level == 2:
                tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                                      weights=[50, 10, 8, 12, 20])[0]
            elif level == 3:
                tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                                      weights=[40, 6, 5, 14, 40])[0]
            else:
                tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                                      weights=[30, 5, 5, 16, 30])[0]
            if tipe == 'bomb':
                char = '*'
                color = '#CCC19A'
            else:
                char = random.choice(string.ascii_uppercase)
                if tipe == 'normal':
                    color = '#00ffff'
                elif tipe == 'bonus':
                    color = '#ffd700'
                elif tipe == 'live':
                    color = '#FFFFE0'
                elif tipe == 'danger':
                    color = '#f80000'

            letter = can.create_text(x, 40, text=char, fill=color, font=('Courier New', 20))
            letters.append({
                'id': letter,
                'type': tipe,
                'char': char,
            })


        def move_letters():
            global lives, m_letters

            for letter in letters[:]:
                can.move(letter['id'], 0, fal_speed)
                y = can.coords(letter['id'])[1]

                if y > heght:
                    can.delete(letter['id'])
                    letters.remove(letter)

                    if letter['type'] in ('normal', 'bonus', 'live'):
                        lives -= 1
                        m_letters += 11
                        update_info()
                        if lives <= 0:
                            game_over()
                            return

            win.after(40, move_letters)


        def key_press(event):
            global score, sp_speed, lives, c_letters

            for letter in letters[:]:
                if letter['char'] == event.char.upper():
                    can.delete(letter['id'])
                    letters.remove(letter)

                    c_letters += 1

                    if letter['type'] == 'normal':
                        score += 1
                    elif letter['type'] == 'live':
                        lives += 1
                    elif letter['type'] == 'bonus':
                        score += 2
                    elif letter['type'] == 'danger':
                        lives -= 1
                    elif letter['type'] == 'bomb':
                        lives -= 3

                    update_level()

                    update_info()
                    if lives <= 0:
                        game_over()
                    return


        def update_info():
            can.itemconfig(info, text=f'Очки:{score} Жизни:{lives} Уровень:{level}')

            if level == 1:
                goal = f'Поймать 15 букв ({c_letters}/15)'

            elif level == 2:
                sec = int(time.time() - start_time)
                goal = f'Прожить 30 секунд ({sec}/30)'

            elif level == 3:
                goal = f'Поймать 35 букв ({c_letters}/35)'

            else:
                sec = int(time.time() - start_time)
                goal = f'Не припустить буквы ({sec}/20)'

            can.itemconfig(go_text, text=goal)


        def game_over():
            can.create_text(width // 2, heght // 2, text='Доступ Запрещен', fill='#f8173e', font=('Courier New', 20))


        def game_loop():
            spawn_letter()
            win.after(sp_speed, game_loop)
            update_info()
            update_level()


        win.bind('<Key>', key_press)
        game_loop()
        move_letters()
        win.mainloop()

    else:
        print('Что то не то')
