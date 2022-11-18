import re


def parser_xml_to_yaml_re(filename: str):
    with open(filename, encoding='utf8') as f:
        file = f.read()
        check2 = re.findall(re.compile(r'<(\w+)>'), file)
        check = re.findall(re.compile(r'</(\w+)>'), file)
        if len(check) != len(check2) or set(check) != set(check2):
            raise AttributeError('XML файл некорректен')

        res = re.sub(re.compile(r'<\?.*>'), '', file)  # удаление служебных тегов
        res = re.sub(re.compile(r'</\w+>'), '', res)  # удаление закрывающихся тегов
        res = re.sub(re.compile(r'>'), r': ', res)  # приведение тегов к виду YAML
        res = re.sub(re.compile(r'<'), '', res)
        res = '\n'.join(filter(lambda x: x.strip(), res.split('\n')))  # удаление пустых строк

    with open('result.yaml', 'w', encoding='utf-8') as f:
        f.write(res)


parser_xml_to_yaml_re('day.xml')
