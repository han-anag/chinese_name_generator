import csv

# Open the .csv file of family name characters and Pinyin
with open('surnames.csv', newline='', encoding='utf-8') as csvfile:
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

    # print(list_names)
    # for name in list_names:
    #     print(list_names.split())
for row in list_names:
    print(row)
# Put names into dictionary
