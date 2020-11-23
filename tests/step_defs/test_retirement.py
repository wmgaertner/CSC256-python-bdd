from pytest_bdd import scenarios, parsers, given, when, then
from pytest_bdd.parsers import string

from retirement import year_input_validation, month_input_validation, calculate_retirement

EXTRA_TYPES = {
    'String': str,
}

CONVERTERS = {
    'year': str,
    'month': str,
    'invalid_year': str,
    'invalid_month': str,
    'valid_year': str,
    'valid_month': str,
    'retirement_age': str,
    'retirement_date': str,
}

scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@given('the user has an invalid year value')
def implicit_invalid_year():
    pass


@when('the user enters it in')
def invalid_year():
    pass


@then(
    parsers.cfparse('the function will return the "{invalid_year:String}" value as not true', extra_types=EXTRA_TYPES))
@then('the function will return the "<invalid_year>" value as not valid')
def invalid_year_validation(invalid_year):
    assert year_input_validation(invalid_year) != True


@given('the user has an invalid month value')
def implicit_invalid_month():
    pass


@when('the user enters it in')
def invalid_year():
    pass


@then(parsers.cfparse('the function will return the "{invalid_month:String}" value as not valid',
                      extra_types=EXTRA_TYPES))
@then('the function will return the "<invalid_month> value as not valid')
def invalid_month_validation(invalid_month):
    assert month_input_validation(invalid_month) != True


@given('the user has a valid year value')
def implicit_valid_year():
    pass


@when('the user enters it in')
def valid_year():
    pass


@then(parsers.cfparse('the function will accept the "{valid_year:String}" value as valid', extra_types=EXTRA_TYPES))
@then('the function will accept the "<valid_year>" value as valid')
def valid_year_validation(valid_year):
    assert year_input_validation(valid_year) is True


@given('the user has a valid month value')
def implicit_valid_month():
    pass


@when('the user enters it in')
def valid_month():
    pass


@then(parsers.cfparse('the function will accept "{valid_month:String}" as valid', extra_types=EXTRA_TYPES))
@then('the function will accept "<valid_month>" as valid')
def valid_month_validation(valid_month):
    assert month_input_validation(valid_month) is True


@given('the program accepts the validation of year and month')
def valid_value_check():
    pass


@when('the program passes on the values')
def call_calculation():
    pass


@then(parsers.cfparse(
    'the program will use the "{year:String}" and "{month:String}" to correctly calculate the'
    ' "{retirement_age:String}"', extra_types=EXTRA_TYPES))
@then('the program will use the "<year>" and "<month>" to correctly calculate the "<retirement_age>"')
def correct_retirement_age_calculation(year, month, retirement_age):
    age, date = calculate_retirement(int(year), int(month))

    assert retirement_age == age
