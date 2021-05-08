import json
import csv

def read_from_file():
    purchases = {}

    with open('res\purchase_log.txt', encoding='utf-8') as information_from_purch_log:

        for line in information_from_purch_log:
            line = line.strip()
            dict = json.loads(line)
            key = dict['user_id']
            value = dict['category']
            if key != 'user_id':
                purchases.setdefault(key,value)

    #print(purchases)
    read_and_dict_from_csv(purchases)

def count_lines_in_file():
    with open('res/visit_log.csv') as f:
        line_count = 0
        for line in f:
            line_count += 1

    #print(line_count)

def read_and_dict_from_csv(purchases): #add category via id
    print(purchases)
    with open('res/visit_log.csv', 'r',encoding='utf-8') as visit_log, open('result/newfile.csv','w',encoding='utf-8') as newfile:
        for row in visit_log:
            line_list = row.strip().split(',')
            if line_list[0] in purchases.keys():
                line_list.append(purchases[line_list[0]])
                add_line = ','.join(line_list)
            elif line_list[0] == 'user_id':
                line_list.append('category')
                add_line = ','.join(line_list)
            else:
                add_line = ','.join(line_list)
            newfile.write(add_line + '\n')
