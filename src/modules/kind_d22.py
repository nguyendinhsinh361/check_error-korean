from src.helpers import helper
from src.helpers import common


class Kind_D22_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E22(self, text_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(text_question):
            arr_error.append(5)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def L22(self, answer, correct_answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L4_contains_enough_words(answer, correct_answer):
            arr_error.append(15)
        if not helper.check_L4_contains_noise_words(answer, correct_answer):
            arr_error.append(16)
        if helper.check_L4_format_sentence(answer):
            arr_error.append(20)
        if helper.check_L4_order_words_diff(answer, correct_answer):
            arr_error.append(83)
        return arr_error

    def M22(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N22(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S22(self, correct_answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(correct_answer):
            arr_error.append(72)
        if not helper.check_L21_muitii_line_breaks(correct_answer):
            arr_error.append(75)
        if not helper.check_S4_pairing_method(correct_answer):
            arr_error.append(31)
        if not helper.check_S4_format_combine_sentences(correct_answer):
            arr_error.append(91)

        return arr_error

    def T22(self, explain, answer, correct_answer, kana_answer, romanji_answer, text_question):
        arr_error = []
        if not helper.check_T6_match_correct_answer(explain, correct_answer):
            arr_error.append(43)
        if not helper.check_T6_form_kana(explain, kana_answer, correct_answer, answer):
            arr_error.append(44)
        if not helper.check_T6_form_romanji(explain, romanji_answer, correct_answer, answer):
            arr_error.append(45)
        if not helper.check_T22_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(86)
        if not helper.check_T4_count_explain(explain, correct_answer):
            arr_error.append(42)
        if not helper.check_T4_format_combine_sentences(explain):
            arr_error.append(92)
        arr_error.append(helper.check_T2_brackets(explain))

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E22(kind_data["text_question"]),
            self.L22(kind_data["answer"], kind_data["correct_answer"]),
            self.M22(kind_data["kana_answer"], kind_data["answer"]),
            self.N22(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S22(kind_data["correct_answer"]),
            self.T22(kind_data["explain"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
