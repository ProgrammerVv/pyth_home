import json

def read_from_file():
    purchases = {}

    with open('res\purchase_log.txt', encoding='utf-8') as information_from_purch_log:

        for line in information_from_purch_log:
            line = line.strip()
            dict_ = json.loads(line)
            key = dict_['user_id']
            value = dict_['category']
            if key != 'user_id':
                purchases.setdefault(key,value)

    print(purchases)
