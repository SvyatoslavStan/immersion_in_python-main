import datetime


def checkdate(day: int, month: int, year: int) -> bool:
    try:
        s = datetime.date(year, month, day)
        return True
    
    except ValueError:
        return False



if __name__ == '__main__':
    day = int(input('ведите дату: '))
    mouth = int(input('ведите месяц: '))
    yaer = int(input('ведите год: '))
    print(checkdate(day, mouth, yaer))
    
