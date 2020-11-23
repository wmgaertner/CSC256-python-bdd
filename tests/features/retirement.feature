Feature: Calculate Retirement
    Calculates retirement age for user
    and calculates the retirement date

    Scenario Outline: Handling Invalid Year Inputs
        Given the user has an invalid year value
        When the user enters it in
        Then the function will return the "<invalid_year>" value as not valid

        Examples: Years
            | invalid_year |
            | 1            |
            | 0            |
            | -1           |
            | a            |
            | 1899         |
            | 2021         |
            | !@#$         |

    Scenario Outline: Handling Invalid Month Inputs
        Given the user has an invalid month value
        When the user enters it in
        Then the function will return the "<invalid_month>" value as not valid

        Examples: Months
            | invalid_month |
            | -1            |
            | 0             |
            | 13            |
            | !@#$          |
            | abc           |


    Scenario Outline: Handling Valid Year Inputs
        Given the user has a valid year value
        When the user enters it in
        Then the function will accept the "<valid_year>" value as valid

        Examples: Years
            | valid_year |
            | 1900       |
            | 1901       |
            | 2000       |
            | 2020       |

    Scenario Outline: Handling Valid Month Inputs
        Given the user has a valid month value
        When the user enters it in
        Then the function will accept "<valid_month>" as valid

        Examples: Months
            | valid_month |
            | 1           |
            | 5           |
            | 10          |
            | 12          |

    Scenario Outline: Calculating Retirement Age
        Given the program accepts the validation of year and month
        When the program passes on the values
        Then the program will use the "<year>" and "<month>" to correctly calculate the "<retirement_age>"

        Examples: Inputs and Outputs
            | year | month | retirement_age    |
            | 1900 | 1     | 65 and 0 months.  |
            | 1937 | 12    | 65 and 0 months.  |
            | 1938 | 3     | 65 and 2 months.  |
            | 1943 | 1     | 66 and 0 months.  |
            | 1954 | 12    | 66 and 0 months.  |
            | 1955 | 1     | 66 and 2 months.  |
            | 1959 | 12    | 66 and 10 months. |
            | 1960 | 1     | 67 and 0 months.  |
            | 2020 | 1     | 67 and 0 months.  |

