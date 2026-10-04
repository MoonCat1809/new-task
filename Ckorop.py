import tkinter as tk
import time
import random
import string

width, heght = 900, 700
sp_speed = 2400
fal_speed=5
comdo=0
score = 0
lives = 5
level=1

start_time = time.time()
c_letters = 0
m_letters = 0


win = tk.Tk()
win.title('Vzlomshik_3000')

can = tk.Canvas(win, width=width, height=heght, bg='#0a0a0a')
can.pack()

info = can.create_text(10, 10, text='Очки:0, Жизни:3, Уровень:1', fill='#ff2400', font=('Courier New', 20),anchor='nw')

go_text = can.create_text(width // 2, 10, text = '', fill = '#808080',font=('Courier New', 16))

letters = []

def update_level():
    global level,fal_speed,sp_speed,start_time,m_letters

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

    if level == 1 :
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
        tipe=random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                             weights = [60, 20, 10, 2, 8])[0]
    elif level == 2:
        tipe=random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                             weights = [50, 10, 8, 12, 20])[0]
    elif level == 3:
        tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                             weights=[40, 6, 5, 14, 40])[0]
    else:
        tipe = random.choices(['normal', 'bonus', 'live', 'danger', 'bomb'],
                             weights=[30, 5, 5, 16, 30])[0]
    if tipe=='bomb':
        char='*'
        color='#CCC19A'
    else:
        char = random.choice(string.ascii_uppercase)
        if tipe=='normal':
            color='#00ffff'
        elif tipe=='bonus':
            color='#ffd700'
        elif tipe=='live':
            color = '#FFFFE0'
        elif tipe == 'danger':
            color = '#f80000'

    letter = can.create_text(x, 40, text=char, fill=color, font=('Courier New', 20))
    letters.append({
        'id':letter,
        'type':tipe,
        'char':char,
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
    global score, sp_speed,lives, c_letters

    for letter in letters[:]:
        if letter['char']== event.char.upper():
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
    can.itemconfig(info, text=f'Очки:{score} Жизни:{lives} Уровень:{level}' )

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

    can.itemconfig(go_text, text = goal)

def game_over():
    can.create_text(width//2, heght//2, text='Доступ Запрещен' , fill='#f8173e', font=('Courier New', 20))

def game_loop():
    spawn_letter()
    win.after(sp_speed, game_loop)
    update_info()
    update_level()

win.bind('<Key>', key_press)
game_loop()
move_letters()
win.mainloop()
