from behave import given, when, then
from func import Unique

@given('I have list [{numbers}]')
def list_of_numbers(context, numbers: list):
    context.numbers = Unique(numbers)

@when('Delete repeating numbers')
def unique_list(context):
    context.list = context.numbers.__next__()

@then('List is unique [{numbers}]')
def res_data(context, numbers: list):
    res = [int(i) for i in numbers.split(',')]
    list_of_nums = context.list
    tmp = []
    for i in list_of_nums:
        if i != ',' and i != ' ':
            tmp.append(int(i))
    uniq_list = list(tmp)
    assert res == uniq_list
