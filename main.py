import requests


def get_the_smartest(list_of_superheroes):
    """
    метод получает json файл из https://akabab.github.io/superhero-api
    и возвращает список супергероев сортированный по параметру intelligence
    in:
    список супергероев
    out:
    список супергероев сортированный по параметру intelligence
    """
    response = requests.get(f'https://akabab.github.io/superhero-api/api/all.json').json()
    superhero_intelligence = {}
    for superhero in response:
        if superhero['name'] in list_of_superheroes:
            superhero_intelligence[superhero['name']] = {'intelligence': superhero['powerstats']['intelligence']}
    return sorted(superhero_intelligence.items(), key=lambda x: x[1]['intelligence'], reverse=True)


def task1():
    """
    Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
    """
    print('Задание 1:\nНужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.\n')
    list_of_superheroes = {'Hulk':            {'intelligence': 0},
                           'Captain America': {'intelligence': 0},
                           'Thanos':          {'intelligence': 0}}
    for name, value in get_the_smartest(list_of_superheroes):
        print(f'Имя супергероя {name}, уровень интеллекта {value["intelligence"]}')


def task2():
    pass


def task3():
    pass


def main():
    task1()
    task2()
    task3()

    
if __name__ == '__main__':
    main()