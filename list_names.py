import csv
import re

# Open the .csv file of family name characters and Pinyin, encode without the byte order mark (BOM)
with open('surnames.csv', newline='', encoding='utf-8-sig') as csvfile:
    names = csv.reader(csvfile)
    # for row in names:
    #    # print(''.join(row))
    #    pass
    #    #print(row)
    
    # An array of strings, each element being a family name
    list_names = []
    for row in names:
        list_names.append(row)
        #print(row)

    print(list_names)

    # print(list_names)
    # for name in list_names:
    #     print(list_names.split())

    # for surname in list_names:
    #     # Remove '\xa0' character if present
    #     if "\xa0" in surname:
    #         surname = surname.replace('\xa0', ' ')
    #     print(surname, type(surname))
# Put names into dictionary
