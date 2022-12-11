def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func_result = func(*args, **kwargs)
        if isinstance(func_result, list):
            for i in func_result:
                print(i)
        elif isinstance(func_result, dict):
            for key, d in func_result.items():
                print('{} = {}'.format(key, d))
        else:
            print(func_result)
        return func_result
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main5():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == '__main__':
    main5()