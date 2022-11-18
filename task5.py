import csv

from xml_to_dict import XMLtoDict


def task5(filename: str):
    with open(filename, 'r', encoding='utf8') as f:
        dictionary = XMLtoDict().parse(f.read())
        result = list()
        for key, value in dictionary.get('schedule').items():
            date = ''
            for k, v in value.items():
                if k == 'day_date':
                    date = v
                    continue
                start = v.get('time', dict()).get('start', '')
                end = v.get('time', dict()).get('end', '')
                type = v.get('body', dict()).get('type', '')
                name = v.get('body', dict()).get('name', '')
                teacher = v.get('body', dict()).get('info', dict()).get('teacher', '')
                place = v.get('body', dict()).get('info', dict()).get('place', '')
                distant = v.get('body', dict()).get('info', dict()).get('distant', '')

                result.append({'date': date,
                               'start': start,
                               'end': end,
                               'type': type,
                               'name': name,
                               'teacher': teacher,
                               'place': place,
                               'distant': distant})

    with open('result.csv', 'w', encoding='utf8') as f:
        d_writer = csv.DictWriter(f, result[0].keys())
        d_writer.writeheader()
        d_writer.writerows(result)


task5('day.xml')
