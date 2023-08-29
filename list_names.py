import csv
import re

# Open the .csv file of family name characters and Pinyin, encode without the byte order mark (BOM)
with open('surnames.csv', newline='', encoding='utf-8-sig') as csvfile:
    names = csv.reader(csvfile)
    # for row in names:
    #    print(''.join(row))
    #    pass
    #    #print(row)
    
    # An array of strings, each element being a family name
    list_surnames = []
    for row in names:
        list_surnames.append(row[0])

    # print(list_surnames)

for surname in list_surnames:
    # Remove '\xa0' character if present
    if "\xa0" in surname:
        surname = surname.replace('\xa0', ' ')
    print(surname)
    
# Put names into dictionary
