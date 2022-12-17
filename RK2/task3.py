from operator import itemgetter

def drivers_sort(one_to_many):
    res = sorted(one_to_many, key=itemgetter(0))
    return res
