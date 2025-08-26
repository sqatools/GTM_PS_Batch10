from datetime import date

date_2 = date(2024, 1, 5)
date_1 = date(2023, 1, 5)

result = (date_2 - date_1).days
print ("Number of Days between the given Dates are: ", result, "days")