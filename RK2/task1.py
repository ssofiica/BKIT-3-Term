def a_surname_drivers(one_to_many):
    res = list(filter(lambda i: i[0][0] == "А", one_to_many))
    return res
