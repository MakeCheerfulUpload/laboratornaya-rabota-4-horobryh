def parse_xml_to_yaml(filename: str):
    result = ''
    TAB = '  '
    with open(filename, 'r',  encoding='utf8') as f:
        text = f.read()
        now_tab_level = 0
        for line in map(str.strip, text.split('\n')):
            writing_tag = False
            now_tag = ''
            last_symbol = ''
            string = ''
            if line.startswith('<?'):
                continue
            if line.startswith('</'):
                now_tab_level -= 1
                continue
            for index, symbol in enumerate(line):
                if symbol == '<':
                    writing_tag = True
                elif last_symbol == '<' and symbol == '/':
                    result += TAB * now_tab_level + now_tag + ': ' + string
                    break
                elif symbol == '>':
                    writing_tag = False
                    if index == len(line) - 1:
                        result += TAB * now_tab_level + now_tag + ':'
                        now_tab_level += 1
                elif writing_tag:
                    now_tag += symbol
                else:
                    string += symbol
                last_symbol = symbol
            result += '\n'
        return result


with open('result.yaml', 'w', encoding='utf8') as f:
    f.write(parse_xml_to_yaml('day.xml'))
