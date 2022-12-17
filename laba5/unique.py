
class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.items = items

    def __next__(self):
        NewData = []
        for i in self.items:
            if not (i in NewData):
                NewData.append(i)
        return NewData

    def __iter__(self):
        return self

def Testing(data):
    D = Unique(data)
    return D.__next__()

def main3():
    data = [1, 3, 1, 2, 5, 2]
    D = Unique(data)
    print(D.__next__())

if __name__ == '__main__':
    main3()