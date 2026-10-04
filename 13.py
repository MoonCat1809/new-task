


import tkinter
import random


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
    two_tip=['normal',random_vibor()]
    for food_type in two_tip:
        while True:
            x = random.randint(2, 21) * rectangle
            y = random.randint(2, 21) * rectangle
            if (x, y) not in snake and (x, y) not in [a[:2]for a in apple]:
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
        can.create_text(400, 400, text='Пфьу щмук нажмите R чтоб переиграть', fill='#a7b309', font=('Times', 20))
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
        if  fool == 'normal':
            balli+=1
        elif fool == 'gold':
            balli+=2
        elif fool == 'poison':
            balli+=1
            if len(snake) > 1:
                snake.pop()
        elif fool == 'speed':
            balli+=1
            speed = max(20,speed-30)
            if speed_timer:
                window.after_cancel(speed_timer)
            speed_timer=window.after(5000,reset_speed)
        elif fool == 'slow':
            balli+=1
            speed = min(300, speed + 30)
            if speed_timer:
                window.after_cancel(speed_timer)
            speed_timer = window.after(5000, reset_speed)
        elif fool == 'texno':
            balli+=0
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
    apple=[]

    balle['text'] = 'Счёт: 0'

    go_snake()
    food_apple()
    go_go()


window.bind('<KeyPress>', upravlenie)

go_snake()
food_apple()
go_go()
window.mainloop()
