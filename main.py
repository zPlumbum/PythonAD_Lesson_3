import datetime
import requests


# Задания №1 и №2
def add_log(old_function):

    def new_function(*args, **kwargs):
        params_args = args
        params_kwargs = kwargs
        result = old_function(*args, **kwargs)

        file_path = input('Введите путь к файлу, в который хотите записать данные: ')
        with open(f'{file_path}', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.today()}\nФункция {old_function.__name__} с параметрами {params_args, params_kwargs} вернула значение {result}\n\n')

        return result

    return new_function


@add_log
def summator(a, b):
    result = a + b
    return result


# Задание №3 (Функция взята из задания №1 Д/з №9 блока "Основы языка программирования Python" )
@add_log
def get_hero_intelligence(name):
    response = requests.get(f'https://www.superheroapi.com/api.php/1565665036954012/search/{name}')
    intelligence = response.json()['results'][0]['powerstats']['intelligence']
    return intelligence


if __name__ == '__main__':
    hero_name = input('Введите имя супергероя: ')
    get_hero_intelligence(hero_name)
