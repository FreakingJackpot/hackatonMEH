import requests


def get_vacancies():
    count = get_vacancies_count()
    dict = {}
    for i in range(int(count / 100)):
        params = {
            'text': 'IT',
            'area': 113,
            'page': 0,
            'per_page': 100,
        }

        data = requests.get('https://api.hh.ru/vacancies', params=params)
        data = data.json()

        for i in data['items']:
            dict[i['name']] = get_key_skills(i['url'])
            print(len(dict.keys()))

    return dict


def get_vacancies_count():
    params = {
        'text': 'IT',
        'area': 113,
        'page': 0,
        'per_page': 100,
    }

    data = requests.get('https://api.hh.ru/vacancies', params=params)
    data = data.json()
    return data['found']


def get_key_skills(url):
    data = requests.get(url)
    data = data.json()
    return [i['name'] for i in data['key_skills']]


params = {
    'text': 'IT',
    'area': 113,
    'page': 0,
    'per_page': 100,
}

print(get_vacancies())

