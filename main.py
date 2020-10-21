import datetime
import requests


# Задание №1
def add_log1(old_function):
    def new_function(*args, **kwargs):

        params_args = args
        params_kwargs = kwargs
        result = old_function(*args, **kwargs)

        with open(f'logs_data.txt', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.today()}\nФункция {old_function.__name__} с параметрами {params_args, params_kwargs} вернула значение {result}\n\n')

        return result
    return new_function


@add_log1
def summator(a, b):
    result = a + b
    return result


# Задание №2
def logs_path(path_to_logs_data):
    def add_log2(old_function):
        def new_function(*args, **kwargs):

            params_args = args
            params_kwargs = kwargs
            result = old_function(*args, **kwargs)

            with open(f'{path_to_logs_data}', 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.today()}\nФункция {old_function.__name__} с параметрами {params_args, params_kwargs} вернула значение {result}\n\n')

            return result
        return new_function
    return add_log2


@logs_path('multiplication_data.txt')
def multiplication(a, b):
    result = a * b
    return result


# Задание №3 (Функция взята из задания №1 Д/з №9 блока "Основы языка программирования Python" )
@add_log1
def get_hero_intelligence(name):
    response = requests.get(f'https://www.superheroapi.com/api.php/1565665036954012/search/{name}')
    intelligence = response.json()['results'][0]['powerstats']['intelligence']
    return intelligence


if __name__ == '__main__':
    # hero_name = input('Введите имя супергероя: ')
    # get_hero_intelligence(hero_name)

    summator(2, 34)
    multiplication(2, 2)


