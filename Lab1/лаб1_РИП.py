
import math

def print_naz(name):
    print(name)

def get_kof(msg):
    while True:
        res= input()
        ri = 0
        try:
            ri = int(res)
            return ri
        except:
            pass

if __name__ == '__main__':
    print_naz(f'Елхимова Ирина,  ИУ5-53Б')
    print ('Введите коэффециенты:')
    a = get_kof('A ')
    b = get_kof('B ')
    c = get_kof('C\n')
    print(f'{a} {b} {c}')

    if a == 0:
        print(f'{b}x^2+{c}=0')
        if -c/b < 0:
            print('Корней нет')
            exit()
        else:
            x1 = math.sqrt(-c/b)
            x2 = math.sqrt(-c/b)
            print(f'x1 ={x1}, x2 = {x2}')
            exit()
    if b == 0:
        print(f'{a}x^4+{c}=0')
        if -c/a > 0:
            y = math.sqrt(-c/a)
            x1 = math.sqrt(y)
            x2 = -math.sqrt(y)
            print(f'x1 = {x1}, x2 = {x2}')
            exit()
        elif -c/a == 0:
            x = 0
            print(f' x = {x}')
            exit()
        else:
            print('Корней нет')
            exit()
    else:
        dis = math.pow(b,2) - 4*a*c
        if dis > 0:
            y1 = (-b + math.sqrt(dis))/(2*a)
            y2 = (-b - math.sqrt(dis))/(2*a)
            if (y1 == 0) and (y2 == 0):
                x = 0
                print(f' x = {x}')
                exit()
            else:
                if (y1 == 0) and (y2 !=0 ):
                    x1 = 0
                    if y2 > 0:
                        x2 = - math.sqrt(y2)
                        x3 = math.sqrt(y2)
                        print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}')
                        exit()
                    else:
                        print(f'x1 = {y1}')
                        exit()
                else:
                    if (y1 != 0 ) and (y2 == 0):
                        x1 = 0
                        if y1 > 0:
                            x2 = -math.sqrt(y1)
                            x3 = math.sqrt(y1)
                            print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}')
                            exit()
                        else:
                            print(f'x1 = {y1}')
                        exit()
                    elif (y1 < 0) and (y2 < 0):
                        print('Корней нет')
                        exit()
                    else:
                        x1 = math.sqrt(y1)
                        x2 = -math.sqrt(y1)
                        x3 = math.sqrt(y2)
                        x4 = -math.sqrt(y2)
                        print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}')
                        exit()
        else:
            if dis == 0:
                y = (-b / (2 * a))
                if y > 0:
                    x1 = math.sqrt(y)
                    x2 = - math.sqrt(y)
                    print(f'x1 = {x1}, x2 = {x2}')
                    exit()
                else:
                    if y == 0:
                        x = 0
                        print(f'x = {x}')
                        exit()
                    else:
                        print('Корней нет')
                        exit()
            else:
                print('Корней нет')
                exit()
             