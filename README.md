# HTTP Server FLASK
>HTTP-server for getting information on geographical objects..
## Реализован проект на Python 3.9.10
В папке проекта предусмотрен файл с пакетами requirements.txt. В целом для работы устанавливался только пакет Flask 2.0.3.
Для запуска сервера на Flask в script.py в конце встроено:
```python
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
```

## Описание разработанных методов
### Метод №1
_The method gets a geonameid and returns information about the city._
_Address:_ 
```web-idl
127.0.0.1:8000/cities?geonameid=id
```
Методу передается числовой параметр (число из первого столбца в наборе данных), по которому проводится поиск на соответствие. Данные о найденном городе возвращаются пользователю в формате json.

### Метод №2
_The method gets the page and the number of cities displayed on the page and returns a list of cities with their information._ 
_Address:_ 
```web-idl
127.0.0.1:8000/citylist?page_number=page&number_of_cities=number
```
Методу передаются 2 числовых параметра объявленных выше (страница и количество городов). По этим параметрам делается срез из списка, полученного в ходе чтения файла RU.txt.
Затем циклом for производится запись в список cities_page_list.

### Метод №3
_The method gets the names of two cities (in Russian) and receives information about the cities found, as well as additionally: which of them is located to the north and what time zone they have (when several cities have the same name, a city with a large population is selected; if the population matches, the first city that comes across is selected)._
_Address:_ 
```web-idl
127.0.0.1:8000/citycompare?city1=Город1&city2=Город2
```
Методу передаются 2 параметра, а именно - имена городов на русском языке. 
Поиск на соответствие производится в третьей колонке набора данных, в котором через запятую перечислено название соответствующего города на разных языках.
В связи с этим производится разделение третьего элемента списка по знаку ",", а затем поиск нужного населенного пункта.

В конце работы функции также предусмотрены условия для нахождения более северного города, сравниваются временные зоны и записываются результаты в список list_with_difference. Данный список возвращается пользователю в качестве ответа от сервера.

### Дополнение
_For the 3rd method, the user is shown not only the difference in time zones, but also how many hours they differ._
В начале скрипта предусмотрен словарь с временными зонами. Значения данного словаря задействуются при расчете разницы во времени. Запись производится в список list_with_difference, который далее возвращается пользователю.



