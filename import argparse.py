import argparse
import re
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Разделить строку на подстроки заданной длины')
    parser.add_argument('-f', '--file', type=str, required=True, help='Путь к входному файлу')
    parser.add_argument('-n', '--max-length', type=int, default=200, help='Максимальная длина каждой подстроки')
    args = parser.parse_args()
    return args

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_string = file.read()
        return input_string
    except Exception as e:
        print(f'Ошибка чтения входного файла: {e}')
        exit()

def split_string(input_string, max_length):
    substrings = []
    current_substring = ""
    pattern = re.compile(r'(@\w+)|(\d{2}\.\d{2}\.\d{4})|(\w+:\/\/\S+)|(.)')
    words = pattern.findall(input_string)
    for word in words:
        if len(current_substring) + len(''.join(word)) > max_length:
            if not current_substring:
                raise Exception(f'Невозможно разделить строку с заданными параметрами: {input_string}')
            substrings.append(current_substring)
            current_substring = ""
        current_substring += ''.join(word)
    substrings.append(current_substring)

    return substrings

def print_substrings(substrings):
    for i, substring in enumerate(substrings):
        print(f'\nSubstring #{i+1}:')
        print(substring)

if __name__ == '__main__':
    args = parse_args()
    input_string = read_input_file(args.file)
    substrings = split_string(input_string, args.max_length)
    print_substrings(substrings)