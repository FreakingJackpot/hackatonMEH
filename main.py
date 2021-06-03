import requests
from collections import Counter


def get_vacancies():
    count = get_vacancies_count()
    dict = {}
    for i in range(2):
        params = {
            'text': 'IT',
            'area': 113,
            'page': i,
            'per_page': 100,
        }

        data = requests.get('https://api.hh.ru/vacancies', params=params).json()

        for i in data['items']:
            if i['name'] in dict:
                tmp = get_key_skills(i['url'])
                counter = dict[i['name']]['counter']
                for word in tmp:
                    counter[word] += 1
                dict[i['name']] = {'key_skills': list(set(get_key_skills(i['url']) + dict[i['name']]['key_skills'])),
                                   'counter': counter}
            else:
                tmp = get_key_skills(i['url'])
                counter = Counter()
                for word in tmp:
                    counter[word] += 1
                dict[i['name']] = {'key_skills': get_key_skills(i['url']), 'counter': counter}
            print(len(dict))
        print(dict)
    return dict


def get_vacancies_count():
    params = {
        'text': 'IT',
        'area': 113,
        'page': 0,
        'per_page': 1,
    }

    data = requests.get('https://api.hh.ru/vacancies', params=params).json()
    return data['found']


def get_key_skills(url):
    data = requests.get(url)
    data = data.json()
    return [i['name'] for i in data['key_skills']]


data = get_vacancies()

"""
with open('vacancies.txt', 'w') as f:
    for i in data.keys():
        str = ''
        c = dict(data[i]['counter'])
        for j in c.keys():
            str += '{} : {}\t'.format(j, c[j])
        f.write(i + ': ' + str + '\n')
"""
