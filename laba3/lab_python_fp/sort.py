def main3():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    result = sorted(data, key=abs, reverse=True)
    print('Result: {}'.format(result))
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print('LambdaResult: {}'.format(result_with_lambda))


if __name__ == '__main__':
    main3()