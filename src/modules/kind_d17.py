from src.helpers import helper
from src.helpers import common


class Kind_D17_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E17(self, text_question):
        arr_error = []
        if not helper.check_E17_structure_translate(text_question):
            arr_error.append(6)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def K17(self, audio):
        arr_error = []
        if not helper.check_K17_has_content(audio):
            arr_error.append(78)
        return arr_error

    def L17(self, answer, correct_answer):
        arr_error = []
        if not helper.check_L17_count_japanese_words(answer):
            arr_error.append(79)
        if not helper.check_L4_contains_enough_words(answer, correct_answer):
            arr_error.append(80)
        if not helper.check_L4_contains_enough_words(answer, correct_answer):
            arr_error.append(81)
        if not helper.check_L17_has_punctuation(answer):
            arr_error.append(82)
        if helper.check_L4_order_words_diff(answer, correct_answer):
            arr_error.append(83)
        return arr_error

    def M17(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N17(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S17(self, correct_answer):
        arr_error = []
        if not helper.check_L17_count_japanese_words(correct_answer):
            arr_error.append(84)

        return arr_error

    def T17(self, explain, text_question, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T17_expression_kanji_of_correct_answer(explain, correct_answer):
            arr_error.append(55)
        if not helper.check_T6_match_correct_answer(explain, correct_answer):
            arr_error.append(41)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        if not helper.check_T2_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(37)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E17(kind_data["text_question"]),
            self.K17(kind_data["audio"]),
            self.L17(kind_data["answer"], kind_data["correct_answer"]),
            self.M17(kind_data["kana_answer"], kind_data["answer"]),
            self.N17(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S17(kind_data["correct_answer"]),
            self.T17(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
