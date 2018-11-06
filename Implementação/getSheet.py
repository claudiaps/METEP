# -*- coding: UTF-8 -*-

import csv
import json
import os
import io

def createFile():
    header = ["name", "year", "month", "qtd"]
    with open('csvfile.csv','w') as file:  
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(header)

def getLabels():
    list_labels = []
    with open('raw_result.json') as f:
        data = json.load(f)
    for i in data:
        if(i['name'] not in list_labels):
            list_labels.append(i['name'])
    return list_labels

def populateSheet(labels):
    row = []
    k = 1

    for label in labels:
        aux = {
            'name': label,
            'year': "",
            'month': "",
            'qdt': ""
        }
        for i in range(0, 60):
            row.append(aux)

    print(row)

    # for i in range (0, 1440):
    #     if(i < 288):
    #         row[i]['year'] = 2012
    #     elif(i > 288 and i < 576):
    #         row[i]['year'] = 2013
    #     elif(i > 576 and i < 864):
    #         row[i]['year'] = 2014
    #     elif(i > 864 and i < 1152):
    #         row[i]['year'] = 2015
    #     else:
    #         row[i]['year'] = 2016

    # for i in range(0, 1440):
    #     if k == 13:
    #         k = 1
    #     row[i]['month'] = k
    #     k = k+ 1

    # for key in row:
    #     if key not in row:
    #         del(row[key])

    # with open('teste.json', 'w') as teste:
    #     json.dump(row, teste)
    
labels = getLabels()
# print (labels)
populateSheet(labels)

