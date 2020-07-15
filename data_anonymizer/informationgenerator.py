import random
import json
import string
from datetime import datetime, timedelta


def get_first_name():
    first_names_file = open('data_anonymizer/assets/first_names_male.json')

    if random.randint(0, 100) > 75:
        first_names_file = open('data_anonymizer/assets/first_names_female.json')

    return random.choice(json.load(first_names_file))


def get_phone_number():
    number = str(random.randint(0, 99999999))
    number = '316' + '0' * (8 - len(number)) + number
    return number


def get_last_name():
    last_names = open('data_anonymizer/assets/last_names.json')
    return random.choice(json.load(last_names))


def get_middle_name():
    middle_names = ['van', 'van de', 'de', 'ter', 'van den']
    number = random.randint(0, 100)
    if number > 65:
        return random.choice(middle_names)
    return ""


def get_email():
    return get_random_word(7) + "@student.bit-academy.nl"


def get_int():
    return random.randint(0, 9999)


def get_string():
    return get_random_word(random.randint(0, 12))


def get_bool():
    number = random.randint(0, 100)
    if number >= 50:
        return 1
    return 0


def get_date(min_year=2000, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def get_marvel_character():
    characters = open('data_anonymizer/assets/marvel_characters.json')
    return random.choice(json.load(characters))


def get_marvel_location():
    locations = open('data_anonymizer/assets/marvel_locations.json')
    return random.choice(json.load(locations))


def get_anonymized_data(column):
    if column["type"] in ["string", "date", "int", "bool"]:
        if "data" in column:
            return column["data"]

    method_name = "get_{}".format(column["type"])
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
        print("invalid type {}".format(column["type"]))
        return
    return method()


def get_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
