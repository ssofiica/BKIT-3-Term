def parks_with_min_drivers_pay(one_to_many):
    list_of_parks = []
    res = []
    for i in one_to_many:
        if i[2] not in list_of_parks:
            list_of_parks.append(i[2])
    for j in list_of_parks:
        min = 100000000
        for i in one_to_many:
            if j == i[2] and i[1] < min:
                min = i[1]
        res.append((j, min))
    return res
