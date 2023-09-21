import random
from list_names import dict_surnames

class chinese_name:
    def __init__(self, first = '', last = '', first_character= '', last_character = ''):
        self.first = first
        self.first_character = first_character
        self.last = last
        self.last_character = last_character
    
    def generate_surname(self):
        #random_surname = random.choice(sorted(dict_surnames))
        random_surname_character = random.choice(list(dict_surnames.keys()))
        random_surname = dict_surnames[random_surname_character]

        self.last_character = random_surname_character
        self.last = random_surname
    
    def return_surname_character(self):
        return self.last_character
    
    def return_surname(self):
        return self.last