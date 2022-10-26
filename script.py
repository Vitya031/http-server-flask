import json
from math import fabs
from flask import Flask, request

app = Flask(__name__)

file = open('RU.txt', 'r', encoding='utf-8')

# Перенос набора данных из файла в список
cities_list = []
for line in file:
    cities_list.append(line.split('\t'))

# Словарь временных зон для вычета разницы времени
timezones = {'Europe/Monaco': -1, 'Europe/Warsaw': -1, 'Europe/Paris': -1, 'Europe/Oslo': -1, 'Europe/Zaporozhye': 0,
             'Europe/Kiev': 0, 'Europe/Vilnius': 0, 'Europe/Riga': 0, 'Europe/Helsinki': 0, 'Europe/Kaliningrad': 0,
             'Europe/Simferopol': 1, 'Europe/Volgograd': 1, 'Europe/Minsk': 1, 'Europe/Kirov': 1, 'Europe/Moscow': 1,
             'Europe/Saratov': 2, 'Asia/Baku': 2, 'Europe/Ulyanovsk': 2, 'Asia/Tbilisi': 2, 'Europe/Astrakhan': 2,
             'Europe/Samara': 2, 'Asia/Aqtobe': 3, 'Asia/Ashgabat': 3, 'Asia/Tashkent': 3, 'Asia/Qyzylorda': 3,
             'Asia/Yekaterinburg': 3, 'Asia/Almaty': 4, 'Asia/Omsk': 4, 'Asia/Barnaul': 5, 'Asia/Novosibirsk': 5,
             'Asia/Novokuznetsk': 5, 'Asia/Tomsk': 5, 'Asia/Hovd': 5, 'Asia/Krasnoyarsk': 5, 'Asia/Ulaanbaatar': 6,
             'Asia/Irkutsk': 6, 'Asia/Shanghai': 7, 'Asia/Khandyga': 7, 'Asia/Tokyo': 7, 'Asia/Chita': 7, 'Asia/Yakutsk': 7,
             'Asia/Ust-Nera': 8, 'Asia/Sakhalin': 9, 'Asia/Vladivostok': 8, 'Asia/Srednekolymsk': 9, 'Asia/Magadan': 9,
             'Asia/Anadyr': 10, 'Asia/Kamchatka': 10}

# Метод №1
@app.route('/cities', methods=['GET'])
def cities():
    idname = int(request.args.get('geonameid'))
    geo_count = len(cities_list)
    low = 0
    high = geo_count - 1
    while low <= high:
        if int(cities_list[low][0]) == idname:
            city_dict = {'geonameid': cities_list[low][0], 'name': cities_list[low][1],
                         'asciiname': cities_list[low][2], 'alternatenames': cities_list[low][3],
                         'latitude': cities_list[low][4], 'longtitude': cities_list[low][5],
                         'feature_class': cities_list[low][6], 'feature_code': cities_list[low][7],
                         'county_code': cities_list[low][8], 'cc2': cities_list[low][9],
                         'admin1_code': cities_list[low][10], 'admin2_code': cities_list[low][11],
                         'admin3_code': cities_list[low][12], 'admin4_code': cities_list[low][13],
                         'population': cities_list[low][14], 'elevation': cities_list[low][15],
                         'dem': cities_list[low][16], 'timezone': cities_list[low][17],
                         'modification_date': cities_list[low][18][:-1]}
            return json.dumps(city_dict, ensure_ascii=False)
        low += 1
    else:
        return 'No such number'


# Метод №2
@app.route('/citylist', methods=['GET'])
def citylist():
    page = int(request.args.get('page_number'))
    number = int(request.args.get('number_of_cities'))
    cities_page_list = cities_list[((page - 1) * number):(page * number)]
    for i in range(len(cities_page_list)):
        cities_page_list[i] = {'geonameid': cities_page_list[i][0], 'name': cities_page_list[i][1],
                               'asciiname': cities_page_list[i][2], 'alternatenames': cities_page_list[i][3],
                               'latitude': cities_page_list[i][4], 'longtitude': cities_page_list[i][5],
                               'feature_class': cities_page_list[i][6], 'feature_code': cities_page_list[i][7],
                               'county_code': cities_page_list[i][8], 'cc2': cities_page_list[i][9],
                               'admin1_code': cities_page_list[i][10], 'admin2_code': cities_page_list[i][11],
                               'admin3_code': cities_page_list[i][12], 'admin4_code': cities_page_list[i][13],
                               'population': cities_page_list[i][14], 'elevation': cities_page_list[i][15],
                               'dem': cities_page_list[i][16], 'timezone': cities_page_list[i][17],
                               'modification_date': cities_page_list[i][18][:-1]}
    return json.dumps(cities_page_list, ensure_ascii=False)


# Метод №3
@app.route('/citycompare', methods=['GET'])
def citycompare():
    city_name_1 = request.args.get('city1')
    city_name_2 = request.args.get('city2')
    find_result = [i for i, name in enumerate(cities_list) if city_name_1 in name[3].split(',')]
    max_population = -1
    for i in find_result:
        if max_population < int(cities_list[int(i)][14]):
            max_population = int(cities_list[int(i)][14])
            city_1 = {'geonameid': cities_list[int(i)][0], 'name': cities_list[int(i)][1],
                      'asciiname': cities_list[int(i)][2], 'alternatenames': cities_list[int(i)][3],
                      'latitude': cities_list[int(i)][4], 'longtitude': cities_list[int(i)][5],
                      'feature_class': cities_list[int(i)][6], 'feature_code': cities_list[int(i)][7],
                      'county_code': cities_list[int(i)][8], 'cc2': cities_list[int(i)][9],
                      'admin1_code': cities_list[int(i)][10], 'admin2_code': cities_list[int(i)][11],
                      'admin3_code': cities_list[int(i)][12], 'admin4_code': cities_list[int(i)][13],
                      'population': cities_list[int(i)][14], 'elevation': cities_list[int(i)][15],
                      'dem': cities_list[int(i)][16], 'timezone': cities_list[int(i)][17],
                      'modification_date': cities_list[int(i)][18][:-1]}
    find_result = [i for i, name in enumerate(cities_list) if city_name_2 in name[3].split(',')]
    max_population = -1
    for i in find_result:
        if max_population < int(cities_list[int(i)][14]):
            max_population = int(cities_list[int(i)][14])
            city_2 = {'geonameid': cities_list[int(i)][0], 'name': cities_list[int(i)][1],
                      'asciiname': cities_list[int(i)][2], 'alternatenames': cities_list[int(i)][3],
                      'latitude': cities_list[int(i)][4], 'longtitude': cities_list[int(i)][5],
                      'feature_class': cities_list[int(i)][6], 'feature_code': cities_list[int(i)][7],
                      'county_code': cities_list[int(i)][8], 'cc2': cities_list[int(i)][9],
                      'admin1_code': cities_list[int(i)][10], 'admin2_code': cities_list[int(i)][11],
                      'admin3_code': cities_list[int(i)][12], 'admin4_code': cities_list[int(i)][13],
                      'population': cities_list[int(i)][14], 'elevation': cities_list[int(i)][15],
                      'dem': cities_list[int(i)][16], 'timezone': cities_list[int(i)][17],
                      'modification_date': cities_list[int(i)][18][:-1]}
    # В этой строке выполняется первое дополнительное задание
    list_with_difference = [city_1, city_2, {'time_difference': int(fabs(timezones[city_1['timezone']] - timezones[city_2['timezone']]))}]
    # Какой город севернее? Проверим по широте
    if city_1['latitude'] > city_2['latitude']:
        # Теперь выполняем проверку на одинаковую временную зону. Если одинаковая, то вышерасчитанная разность должна быть равна нуля.
        if list_with_difference[2].get('time_difference') == 0:
            list_with_difference[2].update({'northern': city_name_1, 'same_timezone': True})
            return json.dumps(list_with_difference, ensure_ascii=False)
        else:
            list_with_difference[2].update({'northern': city_name_1, 'same_timezone': False})
            return json.dumps(list_with_difference, ensure_ascii=False)
    else:
        if list_with_difference[2].get('time_difference') == 0:
            list_with_difference[2].update({'northern': city_name_2, 'same_timezone': True})
            return json.dumps(list_with_difference, ensure_ascii=False)
        else:
            list_with_difference[2].update({'northern': city_name_2, 'same_timezone': False})
            return json.dumps(list_with_difference, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
