import datetime

from task1F import parse_xml_to_yaml
from task2 import task2_with_libs
from task3 import parser_xml_to_yaml_re

results = list()

start = datetime.datetime.now()
for i in range(100):
    parse_xml_to_yaml('day.xml')
results.append(datetime.datetime.now() - start)

start = datetime.datetime.now()
for i in range(100):
    task2_with_libs('day.xml')
results.append(datetime.datetime.now() - start)

start = datetime.datetime.now()
for i in range(100):
    parser_xml_to_yaml_re('day.xml')
results.append(datetime.datetime.now() - start)

print('Собственный код: ' + str(results[0].total_seconds()))
print('Использование библиотек: ' + str(results[1].total_seconds()))
print('Использование регулярных выражений: ' + str(results[2].total_seconds()))
