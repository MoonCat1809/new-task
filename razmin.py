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
