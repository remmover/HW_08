from datetime import datetime, date, timedelta
from collections import defaultdict


def replace_year(str_date):
    try:
        normal_date = datetime.strptime(str_date, '%d, %m, %Y').date()
        current_year = datetime.now().year
        is_leap_year = (current_year % 4 == 0 and current_year %
                        100 != 0) or (current_year % 400 == 0)

        if normal_date.month == 2 and normal_date.day == 29 and not is_leap_year:
            normal_date = date(current_year, 2, 28)
        else:
            normal_date = normal_date.replace(year=current_year)

        return normal_date

    except ValueError as e:
        print(
            f"Error: {str_date} is not a valid date in the format 'dd, mm, yyyy'.")
        return None


def get_birthdays_per_week(b_days):
    today = datetime.now().date()
    week_later = today + timedelta(days=7)
    birthdays = defaultdict(list)

    try:
        users_to_greet = [user for user in b_days if today <=
                          replace_year(user['birthday']) < week_later]

        for user in users_to_greet:
            bd = replace_year(user['birthday'])
            if bd.weekday() in (5, 6):
                birthdays['Monday'].append(user['name'])
            else:
                birthdays[bd.strftime('%A')].append(user['name'])

        for day, birthday_person in birthdays.items():
            if birthday_person:
                print(f"{day} : {', '.join(birthday_person)}")

    except Exception as e:
        print('Check the entered data pls.')


if __name__ == '__main__':
    users = [{'name': 'Vitalia', 'birthday': '16, 02, 2014'},
             {'name': 'Igor', 'birthday': '16, 03, 2015'},
             {'name': 'Nina', 'birthday': '18, 03, 2003'},
             {'name': 'Ylia', 'birthday': '22, 03, 1986'},
             {'name': 'Kira', 'birthday': '29, 02, 2024'},
             {'name': 'Nazar', 'birthday': '18, 09, 2007'},
             {'name': 'Vova', 'birthday': '30, 03, 2000'},
             {'name': 'Tanya', 'birthday': '22, 03, 1977'}]
    
    get_birthdays_per_week(users)
