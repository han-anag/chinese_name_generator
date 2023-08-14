import csv

# Open the .csv file of family name characters and Pinyin
with open('surnames.csv', newline='', encoding='utf-8') as csvfile:
    names = csv.reader(csvfile)
    for row in names:
        print(''.join(row))

# Put names into dictionary
