import json
import sys


def flattern(items):
    for key, value in items.items():
        if isinstance(value, list):
            for i in value:
                yield from flattern(i)
        else:
            yield key, value


def handle_dict(js, grades):
    for key, value in js.items():
        if isinstance(value, list):
            for i in value:
                handle_dict(i, grades)
        else:
            if js.get('value') == "":
                js['value'] = grades[js['id']]


if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as json_tests_file, open(sys.argv[1], 'r') as json_values_file, open(
                'report.json', 'w') as report:
            json_tests = json.load(json_tests_file)
            json_values = json.load(json_values_file)
            seq_values = [x for x in flattern(json_values)]
            result_dict = {seq_values[index - 1][1]: elem[1] for index, elem in enumerate(seq_values) if
                           elem[0] == 'value'}
            handle_dict(json_tests, result_dict)
            json.dump(json_tests, report)
