


from datetime import datetime

def get_days_from_today(date):

    given_date = datetime.strptime(date, '%Y-%m-%d')

    cureent_date = datetime.today()

    delta = cureent_date - given_date

    return delta.days

date = "2021-04-10"
result = get_days_from_today(date)
print('Difference in days = ', result)