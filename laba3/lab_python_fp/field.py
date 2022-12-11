def field(items, *args):
    assert len(args) > 0
    list1 = []
    for item in items:
        tmp_dict = {}
        for arg in args:
            if arg in item:
                if len(args) > 1:
                    tmp_dict[arg] = item[arg]
                else:
                    tmp_dict[0] = item[arg]
        list1.append(tmp_dict)
    return list1

def main1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    list = []
    OurField = field(goods, 'title', 'price')
    print(OurField)


if __name__ == '__main__':
    main1()
