from write_data import count_data


def input_data():
    dct = dict()
    id = count_data("name.csv")
    dct["id"] = id
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartment"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    return
