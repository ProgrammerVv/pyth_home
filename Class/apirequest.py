import requests
from operator import itemgetter

def connection():
    full_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    max_valute_value_name_finder(full_data)

def max_valute_value_name_finder(data): #foo which set the name of the valute with the biggest value
    print(data['Valute'])
    a = (data['Valute'])

    new_list = []

    for k,v in a.items():
        item = (k,v['Value'])
        new_list.append(item)
    maxim_value_in = max(new_list, key =itemgetter(1))[0]
    print(maxim_value_in)









