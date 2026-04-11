year = 2030

month_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


def is_leap_year(year):
    if year % 4 != 0:
        is_leap = False
    else:
        is_leap = True

    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    return is_leap


def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year_value) else 28
    else:
        duration = 31

    return duration


# Новая функция: печатаем даты.
def print_days():
    for day in days:
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if day % 7 == 0:
            print()


def print_header(year_value, month_index):
    print(months[month_index], year_value)
    duration = get_duration(year_value, month_index)
    print('Количество дней:', duration)


# В цикле вызываем функции print_header() и print_days().
for month_number in month_numbers:
    print_header(year, month_number)
    # Добавляем вызов.
    # Теперь для каждого месяца будут печататься строки с датами.
    print_days()
    print()  # Добавим перенос строки после печати каждого месяца.
