import ssetcolor as st

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
