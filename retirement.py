# William Gaertner

import datetime


def main():
    print("Social Security Full Retirement Age Calculator")

    year, month = getUserInput()
    while (year != ""):
        while ((year_input_validation(year) == False) or (month_input_validation(month) == False)):
            year, month = getUserInput()
            if year == "":
                exit()
        else:
            retirementNRA, retirementInfo = calculate_retirement(int(year), int(month))
        print("Your full retirement age is ", retirementNRA)
        print("This will be in ", retirementInfo.strftime("%B of %Y."))

        year, month = getUserInput()


def year_input_validation(yearInput):
    try:
        year = int(yearInput)
        if year < 1900 or year > 2020:
            print("Year must be between 1900 and 2020.")
            return False
        else:
            return True
    except:
        print("Please enter an integer for year.")
        return False


def month_input_validation(monthInput):
    try:
        month = int(monthInput)
        if month < 1 or month > 12:
            print("Month must be between 1 and 12.")
            return False
        return True
    except:
        print("Please enter an integer for month.")
        return False


def getUserInput():
    year = input("\nEnter year of birth or press Enter to exit: ")

    if year == "":
        month = ""
        return year, month

    month = input("Enter month of birth: ")

    return year, month


def calculate_retirement(yearOfBirth, monthOfBirth):
    retirementYear = 0
    retirementMonth = 0
    if (yearOfBirth <= 1937):
        retirementYear = 65
        retirementMonth = 0
    elif (yearOfBirth > 1937 and yearOfBirth < 1943):
        retirementYear = 65
        retirementMonth = abs(1937 - yearOfBirth) * 2
    elif (yearOfBirth >= 1943 and yearOfBirth <= 1954):
        retirementYear = 66
        retirementMonth = 0
    elif (yearOfBirth > 1954 and yearOfBirth < 1960):
        retirementYear = 66
        retirementMonth = abs(1954 - yearOfBirth) * 2
    elif (yearOfBirth >= 1960):
        retirementYear = 67
        retirementMonth = 0

    delta = datetime.timedelta(days=((retirementYear * 365) + ((retirementMonth + 1) * 30.417)))
    retirementInfo = datetime.date(yearOfBirth, monthOfBirth, 1) + delta

    retirementNRA = str(retirementYear) + " and " + str(retirementMonth) + " months."

    return retirementNRA, retirementInfo
