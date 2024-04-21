from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date() #поточна дата
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date() 
        # дата нар. в цьому році
        birthday_this_year = birthday.replace(year=today.year)
        # якщо дн в цьому році вже пройшов
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            # різниця між дн поточною датою
        days_until_birthday = (birthday_this_year - today).days
            # якщо дн протягом наступного тижня
        if 0 <= days_until_birthday <= 7:
                # перевірка на вихідні
            if birthday_this_year.weekday() in (5, 6): # 5 - Субота, 6 - Неділя
                    # Якщо це субота (5), додати 2 дні (неділя, понеділок)
                if birthday_this_year.weekday() == 5:  # Субота
                    birthday_this_year += timedelta(days=2)
                else:  # Неділя
                    birthday_this_year += timedelta(days=1)
                    # Додати ім'я та дату привітання до списку upcoming_birthdays
            upcoming_birthdays.append({
                    "name": user['name'],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                })
    return upcoming_birthdays
        
        #приклад
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]
        
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні: ")
for birthday_info in upcoming_birthdays:
    print(f'{birthday_info["name"]} - {birthday_info["congratulation_date"]}')