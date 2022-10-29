import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_binary_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result

def get_roots(roots):
    root_result = []
    len_roots = len(roots)
    if len_roots == 1:
        if roots[0] > 0:
            root1 = math.sqrt(roots[0])
            root2 = -math.sqrt(roots[0])
            root_result.append(root1)
            root_result.append(root2)
        elif roots[0] == 0:
            root_result.append(roots[0])
    elif len_roots == 2:
        if roots[0] > 0:
            root1 = math.sqrt(roots[0])
            root2 = -math.sqrt(roots[0])
            root_result.append(root1)
            root_result.append(root2)
        elif roots[0] == 0:
            root_result.append(roots[0])
        if roots[1] > 0:
            root3 = math.sqrt(roots[1])
            root4 = -math.sqrt(roots[1])
            root_result.append(root3)
            root_result.append(root4)
        elif roots[0] == 0:
            root_result.append(roots[0])
    return root_result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    binaryroots = get_binary_roots(a, b, c)
    roots = get_roots(binaryroots)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Четыре корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
