
# Task_1

from datetime import datetime

def get_days_from_today(date):

    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        return f"Error: {e}"

    cureent_date = datetime.today()

    delta = cureent_date - given_date

    return delta.days

date = "2021-04-01"
result = get_days_from_today(date)
print('Difference in days = ', result)