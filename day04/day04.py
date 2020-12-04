def data():
    def parse_doc(doc):
        parameters = sum([line.split(" ") for line in doc.split("\n")], [])
        return {param.split(":")[0]: param.split(":")[1] for param in parameters}


    with open("./day04/data", "r") as file:
        return [parse_doc(doc_desc) for doc_desc in file.read().split("\n\n")]

documents = data()

def is_document_valid_part1(document):
    return len(document) == 8 or (len(document) == 7 and not 'cid' in document)

print(sum(is_document_valid_part1(document) for document in documents))

import re
from functools import reduce

def is_byr_valid(document):
    return int(document['byr']) >= 1920 and int(document['byr']) <= 2002

def is_iyr_valid(document):
    return int(document['iyr']) >= 2010 and int(document['iyr']) <= 2020

def is_eyr_valid(document):
    return int(document['eyr']) >= 2020 and int(document['eyr']) <= 2030

def is_hgt_valid(document):
    m = re.match(r"^(\d+)(cm|in)$", document['hgt'])
    if m:
        value, unit = int(m.group(1)), m.group(2)
        if unit == "cm":
            return value >= 150 and value <= 193
        else:
            return value >= 59 and value <= 76
    else:
        return False

def is_hcl_valid(document):
    return re.match(r"^#[a-f0-9]{6}$", document['hcl'])

def is_ecl_valid(document):
    return document['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_pid_valid(document):
    return re.match(r"^[0-9]{9}$", document['pid'])

def is_document_valid_part2(document):
    validators = [
        is_document_valid_part1,
        is_byr_valid,
        is_ecl_valid,
        is_eyr_valid,
        is_hcl_valid,
        is_hgt_valid,
        is_iyr_valid,
        is_pid_valid
    ]

    return reduce(lambda so_far, next_validator: so_far and next_validator(document), validators, True)

print(len([document['pid'] for document in documents if is_document_valid_part2(document)]))