import requests
import yadisk


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


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload_a_file_using_request(self, file_path, file_path_yadisk, replace=False):
        """
        загрузка файла на яндекс диск с помощью библиотеки request
        in:
        file_path - путь к файлу который нужно загрузить
        file_path_yadisk - путь к файлу на яндекс диске
        replace - заменить файл или нет
        """
        base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type':   'application/json',
                   'Accept':         'application/json',
                   'Authorization': f'OAuth {self.token}'}

        response = requests.get(f'{base_url}/upload?path={file_path_yadisk}&overwrite={replace}', headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(response['href'], files={'file': f})
            except KeyError:
                print(response)

    def upload_a_file_using_yadisk(self, file_path: str, file_path_yadisk: str):
        """
        метод загружает файл на яндекс диск
        in:
        file_path - путь к файлу который нужно загрузить
        file_path_yadisk - путь к файлу на яндекс диске
        out:
        True - в случае успешной загрузки
        False - при не валидном токене
        """
        y = yadisk.YaDisk(token=self.token)
        if y.check_token():
            y.upload(file_path, file_path_yadisk)
            return True
        return False


def task1():
    """
    Нужно определить кто самый умный(intelligence) из трех супергероев - Hulk, Captain America, Thanos.
    """
    print('Задание 1:\nНужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.\n')
    list_of_superheroes = {'Hulk':            {'intelligence': 0},
                           'Captain America': {'intelligence': 0},
                           'Thanos':          {'intelligence': 0}}
    for name, value in get_the_smartest(list_of_superheroes):
        print(f'Имя супергероя {name}, уровень интеллекта {value["intelligence"]}')


def task2():
    # Получить путь к загружаемому файлу и токен от пользователя
    print('Задание 2:\nНужно написать программу, которая принимает на вход путь до файла на компьютере'
          'и сохраняет на Яндекс.Диск с таким же именем.\n')
    path_to_file = '...'
    token = '...'
    uploader = YaUploader(token)
    for i in path_to_file:
        uploader.upload_a_file_using_yadisk(i, i.split('/')[-1] + '.txt')
        uploader.upload_a_file_using_request(i, i.split('/')[-1] + '.txt', replace=True)


def task3():
    print('Задание 3:\nНужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг Python.\n')
    base_url = 'https://api.stackexchange.com/2.3'
    response = requests.get(f'{base_url}/questions?fromdate=1658620800&order=desc&max=1658793600&sort=activity&tagged=python&site=stackoverflow').json()
    for item in response['items']:
        print(item['link'])


def main():
    task1()
    task2()
    task3()


if __name__ == '__main__':
    main()