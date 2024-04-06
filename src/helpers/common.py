from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import os


def is_japanese(word):
    return '\u4e00' <= word <= '\u9fff' or '\u3040' <= word <= '\u30ff'

def is_korean(word):
    for char in word:
        if '가' <= char <= '힣':
            return True
    return False

def is_vietnamese(text):
    return not is_japanese(text)


def is_han(word):
    return all('\u4e00' <= char <= '\u9fff' for char in word)


def is_latin(text):
    latin_character = re.compile(r'^[a-zA-Z]+$')
    return bool(latin_character.match(text))


def contains_latin_or_numbers(text):
    latin_or_numbers_pattern = re.compile(r'[a-zA-Z0-9]+')
    return bool(re.search(latin_or_numbers_pattern, text))


def count_han_words(text):
    han_word_count = 0
    clear_text = text.split("[")[0].strip()
    for char in clear_text:
        if is_korean(char):
            han_word_count += 1
    return han_word_count


def count_pair_of_parentheses(text):
    text_sparate = text.split("()")
    return len(text_sparate) - 1


def get_number_tag_p(text):
    if (not contains_html(text)):
        return True
    # Parse the HTML
    soup = BeautifulSoup(text, 'html.parser')

    count_opening_tags = len(soup.find_all('p'))
    count_closing_tags = text.count('</p>')
    return count_opening_tags == count_closing_tags

def get_number_tag_p_for_colum_detail(text):
    if (not contains_html(text)):
        return 0
    # Parse the HTML
    soup = BeautifulSoup(text, 'html.parser')

    count_closing_tags = text.count('</p>')
    return count_closing_tags


def get_text_from_html(text):
    if (not contains_html(text)):
        return text
    # Parse the HTML
    soup = BeautifulSoup(text, 'html.parser')

    result = ''.join(soup.find_all(text=True))
    return result


def get_text_from_html_romaja(text):
    if (not contains_html(text)):
        return text
    # Parse the HTML
    soup = BeautifulSoup(text, 'html.parser')

    result = ''.join([tmp.strip() for tmp in soup.find_all(
        text=True) if contains_latin_or_numbers(tmp.strip())])
    return result


def contains_html(text):
    return bool(re.search(r'<.*?>', text))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def check_brackets(col1_explain, condition):
    explain_jp = re.findall(condition, col1_explain)
    return bool(len(explain_jp))


def check_explain_match_type_1(col1, col2, col3, condition):
    try:
        explain_jp = re.findall(condition, col1)
        if not col2 and not explain_jp:
            return True
        if not explain_jp or not col2:
            return False
        answers = [element.strip()
                   for element in col2.split("\n") if element.strip() != ""]
        explain_final = explain_jp[0].split("[な]")[
            0] if "[な]" in explain_jp[0] else explain_jp[0].split("[な")[0]
        if "[" in explain_final:
            explain_final = explain_jp[0].split("[na]")[0]
        return clean_text(answers[int(col3)-1]) == clean_text(explain_final)
    except Exception as e:
        print(e)
        return False


def check_explain_match_type_2(col1, col2, condition):
    explain_jp = re.findall(condition, col1)
    if not col2 and not explain_jp:
        return True
    if not explain_jp or not col2:
        return False
    return clean_text(remove_special_characters(explain_jp[0]).replace(" ", "")) == clean_text(remove_special_characters(col2).replace(" ", ""))


def flatten_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result


def get_raw_data(path):
    data = []
    with open(path, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def save_data_to_json(data, path):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def convert_json_to_excel(data, path_excel):
    df = pd.DataFrame(data)
    df.to_excel(path_excel, index=False, engine='openpyxl')


def add_sheet_pandas(filename, sheetname, data):
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'

    try:
        if os.path.exists(filename):
            df = pd.DataFrame(data)
            with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, sheet_name=sheetname, index=False)
        else:
            df = pd.DataFrame(data)
            df.to_excel(filename, sheet_name=sheetname, index=False)
    except Exception as e:
        print(e)


def clean_text(text):
    text = text.replace(" ", "")
    return text.strip().rstrip("。").rstrip(".").rstrip("?").rstrip("？").upper()


def contains_kana(text):
    kana_pattern = r'[\u3040-\u309F\u30A0-\u30FFー]+'
    return bool(re.search(kana_pattern, text))


def contains_romaja(text):
    latin_or_special_pattern = re.compile(
        r'^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|\-~`\s\n]+$')
    return bool(latin_or_special_pattern.match(text))


def remove_special_characters(text):
    return re.sub(r'[^\w\s]', '', text)
