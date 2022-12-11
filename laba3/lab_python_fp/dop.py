#1, 2, 3

#1;1 2;4 3;9
# comprehension
# zip
# lambda
#

List = [1,2,3]
list_1 = [(i, i**2) for i in List]
print('First method: {}'.format(list_1))

list_tmp = [i**2 for i in List]
list_2 = list(zip(List, list_tmp))
print('Second method: {}'.format(list_2))

list_3_tmp = list(map(lambda x: x**2, List))
list_3 = list(zip(List, list_3_tmp))
print('Third method: {}'.format(list_3))







