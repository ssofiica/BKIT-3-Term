from random import randint

def gen_random(num_count, begin, end):
    list=[]
    for i in range(0,num_count):
        list.append(randint(begin, end))
    return list

def main2():
    numbers = gen_random(8, 1, 5)
    print(numbers)

if __name__ == '__main__':
    main2()