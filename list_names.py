import csv
import pandas as pd

"""Sets up generation of surnames"""
surnames = pd.read_csv('surnames.csv', encoding='utf8', header=None)

surnames.rename(columns={0: 'Character'}, inplace=True)

#Doing pandas split on the columns misses a few rows for some reason, so do this to make up for it
surnames['Character'] = surnames.apply(lambda row : row['Character'].split(), axis = 1)
surnames['Character'] = surnames.apply(lambda row : ','.join(row['Character']), axis = 1)

#Actually split the column into two
surnames[['Character','Pinyin']] = surnames['Character'].str.split(',', expand=True)

print(surnames)
# TODO: Turn Character and Pinyin columns into dictionary

# # Open the .csv file of family name characters and Pinyin, encode without the byte order mark (BOM)
# with open('surnames.csv', newline='', encoding='utf-8-sig') as csvfile:
#     lastnames = csv.reader(csvfile)
#     # for row in lastnames:
#     #    print(''.join(row))
#     #    pass
#     #    #print(row)
    
#     # An array of strings, each element being a family name
#     list_surnames = []
#     for row in lastnames:
#         list_surnames.append(row[0])

#     print(list_surnames)

# # Remove '\xa0' character if present
# for i in range(len(list_surnames)):
#     if "\xa0" in list_surnames[i]:
#         list_surnames[i] = list_surnames[i].replace(u'\xa0', u' ')

# # print(list_surnames)

# # Put names into dictionary
# dict_surnames = {}
# for surname in list_surnames:
#     dict_surnames[surname[0:surname.find(' ')]] = surname[(surname.find(' ')) + 1:len(surname)]

#print(dict_surnames)

# """Sets up generation of given names"""
# with open('top_first_names_per_decade.csv', newline='', encoding='utf-8-sig') as csvfile:
#     firstnames = csv.reader(csvfile)
#     for row in firstnames:
#        # print('/'.join(row))
#        print(row)
    
#     # An array of strings, each element being a family name
#     list_firstnames = []
#     for row in firstnames:
#         list_firstnames.append(row[0])

# if __name__ == "__main__":
#     print(list_firstnames)