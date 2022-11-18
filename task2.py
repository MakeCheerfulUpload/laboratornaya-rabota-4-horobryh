from xml_to_dict import XMLtoDict
from yaml import dump


def task2_with_libs(filename: str):
    with open(filename) as f:
        dictionary = XMLtoDict().parse(f.read())
    with open('result.yaml', 'w') as f:
        dump(dictionary, f, allow_unicode=True)


task2_with_libs('day.xml')
