from pyparsing import col
from src.helpers import common
import re
from bs4 import BeautifulSoup
import unicodedata

# Lesson
def check_A2_sheetname(lesson_sheetname):
    if (not lesson_sheetname):
        return False
    return True

# Count questions
def check_C2_count_question_increament(count_questions):
    if (not count_questions):
        return False
    return True


# Column text_question
def check_E2_structure_where(text):
    if (not text):
        return False
    check = text.split("\"")
    if (len(check) < 2):
        return False
    return common.is_vietnamese(check[1]) and check[0].strip() == "Chọn"

def check_E3_written_by_korean(text):
    try:
        text = text.strip("\n")
        if (not text):
            return False
        clean_text = common.get_text_from_html(text)
        return any(common.is_korean(element) for element in clean_text)
    except Exception as e:
        return False

def check_E3_has_tag_p_same(text_question):
    if (not text_question):
        return False
    return common.get_number_tag_p(text_question)

def check_E11_appear_only_have_one_han_char(text):
    if (not text):
        return False
    return common.count_han_words(text) == 1


def check_E12_appear_more_two_han_char(text):
    if (not text):
        return False
    return common.count_han_words(text) >= 2


def check_E13_written_by_vietnamese(text):
    try:
        text = text.strip("\n")
        if (not text):
            return False
        text_completed = text.split("(")

        return not check_E3_written_by_korean(text_completed[0])
    except Exception as e:
        return False


def check_E17_structure_translate(text):
    if (not text):
        return False
    check = text.split("\"")
    return common.is_vietnamese(check[1]) and check[0].strip() == "Dịch" and check[2].strip() == ""


def check_E18_contain_a_pair_of_parentheses(text):
    if (not text):
        return False
    return common.count_pair_of_parentheses(text) == 1


def check_E19_contain_more_pair_of_parentheses(text):
    if (not text):
        return False
    return common.count_pair_of_parentheses(text) >= 1


def check_format_tag_p(text):
    if "<p>" in text or "</p>" in text:
        return common.get_number_tag_p(text)
    return True


# Column romaja_question

def check_format_round_brackets(col1, col2):
    round_brackets_col1 = col1.split("()")
    round_brackets_col2 = col2.split("()")
    return len(round_brackets_col1) == len(round_brackets_col2)

def check_F3_match_column(col1, col2):
    if (not col1):
        return False
    words_col1 = [common.remove_special_characters(element.strip()) for element in col1.split(
        "\n") if element.strip() != ""]
    words_col2 = [common.remove_special_characters(element.strip()) for element in col2.split(
        "\n") if element.strip() != ""]
    condition_1 = len(words_col1) == len(words_col2)
    check_html_col1 = check_format_tag_p(col1)
    check_html_col2 = check_format_tag_p(col2)
    check_tag_p_in_two_col = common.get_number_tag_p_for_colum_detail(col1) == common.get_number_tag_p_for_colum_detail(col2)
    condtion_2 = check_html_col1 and check_html_col2 and check_tag_p_in_two_col
    return condition_1 and condtion_2

# Column mean_question

# Column audio

# Checking
def check_H3_have_tag_p_or_h(text):
    if (not text):
        return False
    return bool(re.search(r'<[phPH][^>]*>.*?</[phPH]>', text))


def check_H3_like_column(col1_audio, col2_text_question):
    if (not col1_audio):
        return False
    text_question = col2_text_question.split('[')[0].strip()
    text_question = text_question.replace("\n", "")
    clean_text = common.get_text_from_html(text_question)
    return common.clean_text(clean_text) == common.clean_text(col1_audio)

# Column image


def check_I17_has_content(text):
    if (not text):
        return False
    return bool(text)

# Column answer


def check_J2_has_two_or_four_answers(text):
    if (not text):
        return False
    answer_arr = text.split("\n")
    answer_arr = [common.remove_special_characters(element.strip())
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) == 2 or len(answer_arr) == 4


def check_J3_has_max_four_answers(text):
    if (not text):
        return False
    answer_arr = text.split("\n")
    answer_arr = [common.remove_special_characters(element.strip())
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) <= 4 and len(set(answer_arr)) == len(answer_arr)


def check_J4_contains_enough_words(col1_answer, col2_correct_ans):
    try:
        if (not col1_answer):
            return False
        words_col1 = [element.strip() for element in col1_answer.split(
            "\n") if element.strip() != "" and element[0].strip() != "#"]
        words_col2 = [element.strip() for element in col2_correct_ans.split(
            "\n") if element.strip() != "" and element[0].strip() != "#"]
        contains_all = all(words_col1.count(item) >= (words_col2.count(item))/2 for item in words_col2)   
        return all(element in words_col1 for element in words_col2) and contains_all
    except Exception as e:
        print(col1_answer, col2_correct_ans)


def check_J4_contains_noise_words(col1_answer, col2_correct_ans):
    try:
        if (not col1_answer):
            return False
        words_col1 = [common.remove_special_characters(element.strip()) for element in col1_answer.split(
            "\n") if element.strip() != ""]
        words_col2 = [common.remove_special_characters(element.strip()) for element in col2_correct_ans.split(
            "\n") if element.strip() != "" and element[0].strip() != "#"]
        return not len(set(words_col1)) < len(set(words_col2))
    except Exception as e:
        return False


def check_J4_format_sentence(text):
    if (not text):
        return False
    words = [common.remove_special_characters(element.strip())
             for element in text.split("\n") if element.strip() != ""]
    return any(bool(text[len(ele) - 1] == ".") for ele in words)


def check_J4_order_words_diff(col1_answer, col2_correct_ans):
    try:
        if (not col1_answer):
            return False
        words_col1 = [common.remove_special_characters(element.strip()) for element in col1_answer.split(
            "\n") if element.strip() != ""]
        words_col2 = [common.remove_special_characters(element.strip()) for element in col2_correct_ans.split(
            "\n") if element.strip() != ""]

        return all(words_col2[i] == words_col1[i] for i in range(len(words_col2)))
    except Exception as e:
        return False

def check_J9_audio_contains_answers_accept_dots(col1_answer, col2_audio):
    if (not col1_answer):
        return False
    words_col1 = [common.remove_special_characters(element.strip()) for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element.rstrip(".")) == common.remove_special_characters(str(col2_audio.rstrip(".")))
               for element in words_col1)


def check_J13_audio_contains_answers(col1_answer, col2_audio):
    if (not col1_answer):
        return False
    words_col1 = [common.remove_special_characters(element.strip()) for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element) == common.remove_special_characters(str(col2_audio)) for element in words_col1)


def check_J17_count_korean_words(text):
    if (not text):
        return False
    words = [common.remove_special_characters(element.strip())
             for element in text.split("\n") if element.strip() != ""]
    return all(len(element) <= 2 for element in words)


def check_J17_has_punctuation(text):
    if (not text):
        return False
    words = [common.remove_special_characters(element.strip())
             for element in text.split("\n") if element.strip() != ""]
    words_str = "".join(words)
    return all(common.is_japanese(element) for element in words_str)


def check_J19_structure_pair_of_parentheses(text):
    if (not text):
        return False
    return (text.startswith('(') and text.endswith('）')) or text.startswith('(') and text.endswith(')')


def check_J21_muitii_line_breaks(text):
    try:
        if (not text):
            return False
        line = [common.remove_special_characters(element.strip())
                for element in text.split("\n") if element.strip() != ""]
        return len(line) > 1
    except Exception as e:
        return False

# Column Image_answer

def check_M16_two_or_four_img(image_answer):
    # Pending
    return True

# Column correct_answer


def check_N2_type_number(text):
    if (not text):
        return False
    return common.is_number(text)


def check_N4_pairing_method(text):
    try:
        if (not text):
            return False
        pairing_method = [common.remove_special_characters(element.strip()) for element in text.split(
            "\n") if element.strip() != "" and element[0].strip() != "#"]
        return len(pairing_method) >= 1
    except Exception as e:
        return False


def check_N4_format_combine_sentences(col1_correct_answer):
    try:
        if (not col1_correct_answer):
            return False
        answer_arr = [ele for ele in col1_correct_answer.split("\n") if ele]
        check = True
        for tmp in answer_arr:
            if (tmp.startswith("#")):

                check = bool(tmp.strip() == "###")
                if (not check):
                    return check
        return check
    except Exception as e:
        return False


def check_N10_like_audio_question(col1_correct_answer, col2_audio):
    try:
        if (not col1_correct_answer):
            return False
        words_col1 = [common.remove_special_characters(element.strip()) for element in col1_correct_answer.split(
            "\n") if element.strip() != ""]
        words_col1_completed = "".join(words_col1)
        return common.clean_text(words_col1_completed) == common.clean_text(common.remove_special_characters(col2_audio.replace(" ", "")))
    except Exception as e:
        return False


def check_N13_type_number_and_like_number_audio(col1_correct_answer, col2_answer, col3_audio):
    try:
        if (not col1_correct_answer):
            return False
        answer_arr = [common.remove_special_characters(element.strip()) for element in col2_answer.split(
            "\n") if element.strip() != ""]
        return common.is_number(col1_correct_answer) and common.clean_text(answer_arr[(int(col1_correct_answer) - 1)]) == common.clean_text(common.remove_special_characters(col3_audio))
    except Exception as e:
        return False


def check_N14_correct_answer_like_audio(col1_correct_answer, col2_audio):
    if (not col1_correct_answer):
        return False
    line = [common.remove_special_characters(element.strip())
            for element in col1_correct_answer.split("\n") if element.strip() != ""]
    completed_text = "".join(line)
    return common.clean_text(completed_text) == common.clean_text(common.remove_special_characters(col2_audio))


def check_N19_correct_answer_has_pair_of_parentheses_and_like_answer(col1_correct_answer, col2_answer):
    if (not col1_correct_answer):
        return False
    try:
        matches_correct_answer = re.findall(r'\((.*?)\)', col1_correct_answer)
        matches_answer = re.findall(r'\((.*?)\)', col2_answer)
        if (not matches_answer):
            matches_answer = re.findall(r'\((.*?)\）', col2_answer)
        matches_correct_answer = [
            common.remove_special_characters(element.strip()) for element in matches_correct_answer if element.strip() != ""]
        matches_answer = [common.remove_special_characters(element.strip())
                          for element in matches_answer if element.strip() != ""]
        open_count = col1_correct_answer.count('(')
        close_count = col1_correct_answer.count(')')
        indices = [matches_correct_answer.index(
            item) for item in matches_answer]
        return bool(open_count > 1 and close_count > 1 and indices)
    except Exception as e:
        return False


# Column explain

def check_O2_brackets(col1_explain):
    if (not col1_explain):
        return False
    arr_error = []
    if (not check_O2_angle_brackets(col1_explain)):
        arr_error.append(81)
    elif (not check_O2_round_brackets(col1_explain)):
        arr_error.append(82)
    return arr_error


def check_O2_angle_brackets(col1_explain):
    if (not col1_explain):
        return False
    condition = r'\{\{(.*?)\}\}'
    return common.check_brackets(col1_explain, condition)

def check_O2_round_brackets(col1_explain):
    if (not col1_explain):
        return False
    condition = r'\(\((.*?)\)\)'
    return common.check_brackets(col1_explain, condition)


def check_O2_explain_match_answer_and_correct_answer_type_1(col1_explain, col2_answer, col3_correct_answer):
    if (not col1_explain):
        return False
    condition = r'\{\{(.*?)\}\}'
    if (col2_answer and not col3_correct_answer):
        return False
    return common.check_explain_match_type_1(col1_explain, col2_answer, col3_correct_answer, condition)


def check_O2_explain_match_answer_and_romaja_answer_type_1(col1_explain, col2_romaja_answer, col3_correct_answer):
    if (not col1_explain):
        return False
    condition = r'\(\((.*?)\)\)'
    if (col2_romaja_answer and not col3_correct_answer):
        return False
    return common.check_explain_match_type_1(
        col1_explain, col2_romaja_answer, col3_correct_answer, condition)


def check_O2_explain_mean_like_text_question_type_1(col1_explain, col2_text_question):
    if (not col1_explain):
        return False
    check = col2_text_question
    if (len(col2_text_question.split("\"")) > 1):
        check = col2_text_question.split("\"")[1].strip()
    explain_text_question = col1_explain.split("))")
    if (len(explain_text_question) < 2):
        explain_text_question = col1_explain.split("}}")
    explain_text_question_final = explain_text_question[-1]
    check = unicodedata.normalize('NFC', check)
    explain_text_question_final = unicodedata.normalize(
        'NFC', explain_text_question_final)
    return common.clean_text(check) in common.clean_text(explain_text_question_final)


def check_O3_explain_mean_like_text_question_type_2(col1_explain, col2_text_question):
    if (not col1_explain):
        return False
    check_tag_p = bool(re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    col2_text_question_clean = col2_text_question
    if check_tag_p:
        col2_text_question_clean = common.get_text_from_html(
            col2_text_question)
    col2_text_question_clean = col2_text_question_clean.replace("\n", "")
    condition = r'\{\{(.*?)\}\}'

    return common.check_explain_match_type_2(
        col1_explain, col2_text_question_clean, condition)


def check_O3_explain_mean_like_romaja_question_type_2(col1_explain, col2_romaja_question):
    if (not col1_explain):
        return False
    check_tag_p = bool(
        re.search(r'<[pP][^>]*>.*?</[pP]>', col2_romaja_question))
    col2_romaja_question_clean = col2_romaja_question
    if check_tag_p:
        col2_romaja_question_clean = common.get_text_from_html_romaja(
            col2_romaja_question)
    col2_romaja_question_clean = col2_romaja_question_clean.replace("\n", "")
    condition = r'\(\((.*?)\)\)'

    return common.check_explain_match_type_2(
        col1_explain, col2_romaja_question_clean, condition)


def check_O3_explain_mean_match_correct_answer_type_2(col1_explain, col2_answer, col3_correct_answer):
    if (not col1_explain):
        return False
    try:
        explain_answer = col1_explain.split("))")
        if (len(explain_answer) < 2):
            explain_answer = col1_explain.split("}}")
        answers = [element.strip()
                   for element in col2_answer.split("\n") if element.strip() != ""]
        return common.clean_text(answers[int(col3_correct_answer) - 1]) in common.clean_text(explain_answer[-1])
    except Exception as e:
        return False


def check_O4_explain_mean_like_text_question_type_2(col1_explain, col2_text_question):
    if (not col1_explain):
        return False
    count_explain = [
        tmp for tmp in col1_explain.split("###") if tmp]
    check = False
    for explain in count_explain:
        check = check_O3_explain_mean_like_text_question_type_2(
            explain, col2_text_question)
    return check


def check_O4_explain_mean_like_romaja_question_type_2(col1_explain, col2_romaja_question):
    if (not col1_explain):
        return False
    count_explain = [
        tmp for tmp in col1_explain.split("###") if tmp]
    check = False
    for explain in count_explain:
        check = check_O3_explain_mean_like_romaja_question_type_2(
            explain, col2_romaja_question)
    return check


def check_O4_explain_mean_match_correct_answer_type_3(col1_explain, col2_correct_answer):
    try:
        if (not col1_explain):
            return False
        count_explain = [
            tmp for tmp in col1_explain.split("###") if tmp]
        count_correct_answer = [
            common.remove_special_characters(tmp) for tmp in col2_correct_answer.split("###") if tmp]
        check = False
        for explain, correct_answer in zip(count_explain, count_correct_answer):
            explain_answer = explain.split("))")
            if (len(explain_answer) < 2):
                explain_answer = explain.split("}}")
            answers = [element.strip()
                    for element in correct_answer.split("\n") if element.strip() != ""]
            explain_answer_completed = common.remove_special_characters(
                explain_answer[-1])
            check = common.clean_text(" ".join(answers)) == common.clean_text(
                explain_answer_completed)
        return check
    except Exception as e:
        return False


def check_O4_format_combine_sentences(col1_explain):
    if (not col1_explain):
        return False
    return check_N4_format_combine_sentences(col1_explain)


def check_O4_count_explain(col1_explain, col2_correct_answer):
    try:
        if (not col1_explain):
            return False
        count_explain = [
            tmp for tmp in col1_explain.split("###") if tmp]
        count_correct_answer = [
            tmp for tmp in col2_correct_answer.split("###") if tmp]
        return len(count_explain) == len(count_correct_answer)
    except Exception as e:
        return False

# New Logic
def check_O5_check_like_text_question(explain, text_question):
    if (not explain):
        return False
    explain_answer = explain.split("))")
    if (len(explain_answer) < 2):
        explain_answer = explain.split("}}")
    explain_answer_completed = explain_answer[-1].split("(")
    return explain_answer_completed[0].strip() == text_question
    
def check_O5_check_mean_vietnamese(explain):
    if (not explain):
        return False
    explain_answer = explain.split("))")
    if (len(explain_answer) < 2):
        explain_answer = explain.split("}}")
    explain_answer_completed = explain_answer[-1].split("(")
    return check_E13_written_by_vietnamese(explain_answer_completed[0].strip().rstrip("."))


def check_O6_match_correct_answer(col1_explain, col2_correct_answer):
    try:
        if (not col1_explain):
            return False
        count_explain = [
            tmp for tmp in col1_explain.split("###") if tmp]
        count_correct_answer = [common.remove_special_characters(
            tmp) for tmp in col2_correct_answer.split("###") if tmp]
        check = False
        for explain, correct_answer in zip(count_explain, count_correct_answer):
            correct_answer_arr = [common.remove_special_characters(element.strip()) for element in correct_answer.split(
                "\n") if element.strip() != ""]
            explain_ko = re.findall(r'\{\{(.*?)\}\}', explain)
            explain_ko_completed = common.remove_special_characters(
                explain_ko[0]) if len(explain_ko) > 0 else ""
            check = common.clean_text(explain_ko_completed.replace(" ", "")) == common.clean_text(
                "".join(correct_answer_arr))
        return check
    except Exception as e:
        return False


def check_O6_form_romaja(col1_explain, col2_romaja_answer, col3_correct_answer, col4_answer):
    if (not col1_explain):
        return False
    try:
        count_explain = [
            tmp for tmp in col1_explain.split("###") if tmp]
        count_correct_answer = [common.remove_special_characters(
            tmp) for tmp in col3_correct_answer.split("###") if tmp]
        check = False
        for explain, correct_answer in zip(count_explain, count_correct_answer):
            check = check_O10_form_romaja(
                explain, col2_romaja_answer, correct_answer, col4_answer)
        return check
    except Exception as e:

        return False


def check_O9_explain_like_audio(col1_explain, audio):
    if (not col1_explain):
        return False
    explain_ko = re.findall(r'\{\{(.*?)\}\}', col1_explain)
    if not audio and not explain_ko:
        return True
    if not explain_ko or not audio:
        return False
    return common.clean_text(explain_ko[0].strip("～").split('[な]')[0]) == common.clean_text(audio.strip("～"))


def check_O10_form_romaja(col1_explain, col2_romaja_answer, col3_correct_answer, col4_answer):
    if (not col1_explain):
        return False
    try:
        explain_romaja = re.findall(r'\(\((.*?)\)\)', col1_explain)
        explain_romaja_completed = common.remove_special_characters(
            explain_romaja[0])
        romaja_answer_arr = [
            common.clean_text(common.remove_special_characters(ele.strip("\r").strip())) for ele in col2_romaja_answer.split("\n") if ele]
        correct_answer_arr = [
            common.remove_special_characters(ele.strip("\r").strip()) for ele in col3_correct_answer.split("\n") if ele]
        answer_arr = [common.remove_special_characters(
            ele.strip("\r").strip()) for ele in col4_answer.split("\n") if ele]
        index_romaja_correct_answer_arr = [
            answer_arr.index(item.strip("\r").strip()) for item in correct_answer_arr]
        romaja_correct_answer = " ".join(
            [romaja_answer_arr[ele] for ele in index_romaja_correct_answer_arr])
        return romaja_correct_answer.replace(" ", "") == common.clean_text(
            explain_romaja_completed).replace(" ", "")
    except Exception as e:
        return False


def check_O13_explain_mean_like_text_question_type_1(col1_explain, col2_text_question):
    col2_text_question = col2_text_question.replace("\n", " ")
    if (not col1_explain):
        return False
    check_tag_p = bool(
        re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    col2_text_question_clean = col2_text_question
    if check_tag_p:
        col2_text_question_clean = common.get_text_from_html(
            col2_text_question)
    text_question_clean = col2_text_question_clean
    if (len(col2_text_question.split("\"")) > 1):
        text_question_clean = col2_text_question.split("\"")[1].strip()
    explain_text_question = col1_explain.split("))")
    if (len(explain_text_question) < 2):
        explain_text_question = col1_explain.split("}}")
    explain_text_question_final = explain_text_question[-1].split("(tính từ đuôi い)")[
        0]
    explain_text_question_final = explain_text_question_final.split("(tính từ đuôi な)")[
        0]
    text_question_clean = unicodedata.normalize('NFC', text_question_clean)
    explain_text_question_final = unicodedata.normalize(
        'NFC', explain_text_question_final)
    return common.clean_text(text_question_clean) in common.clean_text(explain_text_question_final)


def check_O15_form_romaja_of_audio(col1_explain, col2_audio):
    if (not col1_explain):
        return False
    try:
        romaja_ko = re.findall(r'\(\((.*?)\)\)', col1_explain)
        return common.contains_romaja(romaja_ko[0])
    except Exception as e:
        return False


def check_O17_expression_kanji_of_correct_answer(col1_explain, col2_correct_answer):
    # Pending
    if (not col1_explain):
        return False
    explain_ko = re.findall(r'\{\{(.*?)\}\}', col1_explain)
    check_ko = check_E3_written_by_korean(explain_ko[0])
    return check_ko


def check_O18_complete_sentences_answer_combining_correct_answer(col1_explain, col2_correct_answer, col3_text_question, col4_answer):
    if (not col1_explain):
        return False
    try:
        explain_ko = re.findall(r'\{\{(.*?)\}\}', col1_explain)
        text_question_clean = common.get_text_from_html(col3_text_question)
        text_question_clean = text_question_clean.replace("\n", "")
        separate_text_question = text_question_clean.split("()")
        if (not separate_text_question):
            separate_text_question = text_question_clean.split("(）")
        answer_arr = [common.remove_special_characters(element.strip()) for element in col4_answer.split(
            "\n") if element.strip() != ""]
        correct_answer_completed = f'{separate_text_question[0]}{answer_arr[int(col2_correct_answer) - 1]}{separate_text_question[1]}'
        return common.clean_text(explain_ko[0]) == common.clean_text(correct_answer_completed)
    except Exception as e:
        return False


def check_O18_complete_sentences_answer_combining_romaja_answer(col1_explain, col2_correct_answer, col3_romaja_question, col4_romaja_answer):
    if (not col1_explain):
        return False
    try:
        romaja_explain_ko = re.findall(r'\(\((.*?)\)\)', col1_explain)
        romaja_question_clean = common.get_text_from_html_romaja(
            col3_romaja_question)
        romaja_question_clean = romaja_question_clean.replace("\n", "")
        separate_romaja_question = romaja_question_clean.split("()")
        if (not separate_romaja_question):
            separate_romaja_question = romaja_question_clean.split("(）")
        romaja_answer_arr = [common.remove_special_characters(element.strip()) for element in col4_romaja_answer.split(
            "\n") if element.strip() != ""]
        correct_answer_completed = f'{separate_romaja_question[0]}{romaja_answer_arr[int(col2_correct_answer) - 1]}{separate_romaja_question[1]}'
        return common.clean_text(romaja_explain_ko[0]).replace(" ", "") == common.clean_text(correct_answer_completed).replace(" ", "")
    except Exception as e:
        return False


def check_O19_complete_sentences_text_combining_correct_answer(col1_explain, col2_correct_answer, col3_text_question, col4_answer):
    if (not col1_explain):
        return False
    try:
        matches_correct_answer = re.findall(r'\((.*?)\)', col2_correct_answer)
        matches_answer = re.findall(r'\((.*?)\)', col4_answer)
        if (not matches_answer):
            matches_answer = re.findall(r'\((.*?)\）', col4_answer)

        matches_correct_answer_final = []
        for i, item in enumerate(matches_correct_answer):
            if item != "":
                matches_correct_answer_final.append(matches_answer.pop(0))
            else:
                matches_correct_answer_final.append("")

        matches_correct_answer_final.append("")
        text_question_clean = common.get_text_from_html(col3_text_question)
        text_question_clean = text_question_clean.replace("\n", "").replace(" ", "")
        text_explain_ko = re.findall(r'\{\{(.*?)\}\}', col1_explain)
        separate_text_question = text_question_clean.split("()")
        if (not separate_text_question):
            separate_text_question = text_question_clean.split("(）")
        correct_answer_completed = ""
        for tmp1, tmp2 in zip(separate_text_question, matches_correct_answer_final):
            correct_answer_completed += f'{tmp1}{tmp2}'
        return common.clean_text(correct_answer_completed) == common.clean_text(text_explain_ko[0].replace(" ", ""))
    except Exception as e:
        return False

def check_O19_complete_sentences_text_combining_romaja_answer(col1_explain, col2_correct_answer, col3_romaja_question, col4_romaja_answer):
    if (not col1_explain):
        return False
    try:
        matches_correct_answer = re.findall(r'\((.*?)\)', col2_correct_answer)
        matches_answer = re.findall(r'\((.*?)\)', col4_romaja_answer)
        if (not matches_answer):
            matches_answer = re.findall(r'\((.*?)\）', col4_romaja_answer)

        matches_correct_answer_final = []
        for i, item in enumerate(matches_correct_answer):
            if item != "":
                matches_correct_answer_final.append(
                    f' {matches_answer.pop(0)}')
            else:
                matches_correct_answer_final.append("")
        matches_correct_answer_final.append("")
        romaja_question_clean = common.get_text_from_html_romaja(
            col3_romaja_question)
        romaja_question_clean = romaja_question_clean.replace("\n", "").replace(" ", "")
        romaja_explain_ko = re.findall(r'\(\((.*?)\)\)', col1_explain)
        separate_romaja_question = romaja_question_clean.split("()")
        if (not separate_romaja_question):
            separate_romaja_question = romaja_question_clean.split("(）")
        separate_romaja_question = [common.remove_special_characters(tmp.rstrip())
                                     for tmp in separate_romaja_question]
        correct_answer_completed = ""
        for tmp1, tmp2 in zip(separate_romaja_question, matches_correct_answer_final):
            correct_answer_completed += f'{tmp1}{tmp2}'
        return common.clean_text(correct_answer_completed).replace(" ", "") == common.clean_text(common.remove_special_characters(romaja_explain_ko[0])).replace(" ", "")
    except Exception as e:
        return False


def check_O21_complete_sentences_drop_text_combining_correct_answer(col1_explain, col2_correct_answer, col3_answer):
    if (not col1_explain):
        return False
    try:
        text_explain_ko = re.findall(r'\{\{(.*?)\}\}', col1_explain)
        correct_answer = [tmp.strip("\r").strip() for index, tmp in enumerate(
            col3_answer.split("\n")) if index != int(col2_correct_answer) - 1 and tmp != ""]
        correct_answer_completed = "".join(correct_answer)
        return common.clean_text(common.remove_special_characters(text_explain_ko[0])) == common.clean_text(correct_answer_completed)
    except Exception as e:
        return False


def check_O21_complete_sentences_drop_text_combining_romaja_answer(col1_explain, col2_correct_answer, col3_romaja_answer):
    if (not col1_explain):
        return False
    try:
        romaja_explain_ko = re.findall(r'\(\((.*?)\)\)', col1_explain)
        correct_answer = [tmp.strip("\r").strip() for index, tmp in enumerate(
            col3_romaja_answer.split("\n")) if index != int(col2_correct_answer) - 1 and tmp != ""]
        correct_answer_completed = " ".join(correct_answer)
        return common.clean_text(common.remove_special_characters(romaja_explain_ko[0])).replace(" ", "") == common.clean_text(correct_answer_completed).replace(" ", "")
    except Exception as e:
        return False


def check_O22_explain_mean_like_text_question_type_1(col1_explain, col2_text_question):
    if (not col1_explain):
        return False
    count_explain = [
        tmp for tmp in col1_explain.split("###") if tmp]
    check_tag_p = bool(
        re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    col2_text_question_clean = col2_text_question
    if check_tag_p:
        col2_text_question_clean = common.get_text_from_html(
            col2_text_question)
    text_question_clean = col2_text_question_clean
    text_question_clean = text_question_clean.replace("\n", "")

    if (len(col2_text_question.split("\"")) > 1):
        text_question_clean = col2_text_question.split("\"")[1].strip()
    check = False
    for explain in count_explain:
        explain_text_question = explain.split("))")
        if (len(explain_text_question) < 2):
            explain_text_question = explain.split("}}")

        check = common.clean_text(text_question_clean) in common.clean_text(
            explain_text_question[-1])
    return check


# Column explain_grammar
def check_Q3_explain_grammar(col1_explain_grammar, col2_text_question):
    check_tag_p = bool(re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    if check_tag_p and not col1_explain_grammar:
        return False
    return True


def check_Q3_number_explain_grammar(col1_explain_grammar, col2_text_question):
    count_tag_p = col2_text_question.count("<p>")
    if (not col1_explain_grammar and not bool(count_tag_p)):
        return True
    count_explain_grammar = col1_explain_grammar.split("###")
    return count_tag_p == len(count_explain_grammar)

def check_increasing_sequences(arr):
    increasing_sequences = []
    current_sequence = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_sequence.append(arr[i])
        else:
            increasing_sequences.append(current_sequence)
            current_sequence = [arr[i]]

    increasing_sequences.append(current_sequence)

    return increasing_sequences

def is_increasing_and_complete(subarray):
    expected_sequence = set(range(1, len(subarray) + 1))
    return len(subarray) == len(expected_sequence) and set(subarray).issubset(expected_sequence)


def check_arrays(arrays):
    data = check_increasing_sequences(arrays)
    return all(is_increasing_and_complete(subarray) for subarray in data)