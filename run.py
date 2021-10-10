from simple_ball import simple_ball
from break_out import break_out

def main():
    print('1. Simple ball\n2. Break out')
    cmd = input('Введите 1 или 2, для выбора: ').strip()
    if cmd == '1': simple_ball()
    else: break_out()


if __name__ == '__main__':
    main()
