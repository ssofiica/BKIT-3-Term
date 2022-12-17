from radish import given, when, then
from unique import Unique

@given("I have list {list:g}")
def have_list(list):
    D = Unique(list)

@when("Delete repeating numbers")
def delete_numbers(have_list):
    have_list.__next__()

@then("List is {result:g}")
def expect_result(have_list, result):
    assert have_list == result