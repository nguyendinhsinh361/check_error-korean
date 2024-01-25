from src.helpers import helper
from src.helpers import common


class Kind_D10_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def J10(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        return arr_error

    def L10(self, answer, correct_answer):
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

    def M10(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N10(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S10(self, correct_answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(correct_answer):
            arr_error.append(72)
        if not helper.check_L21_muitii_line_breaks(correct_answer):
            arr_error.append(75)
        if not helper.check_S10_like_audo_question(correct_answer, audio):
            arr_error.append(33)
        return arr_error

    def T10(self, explain, audio, correct_answer, kana_answer, romanji_answer, answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio(explain, audio):
            arr_error.append(46)
        if not helper.check_T10_form_kana(explain, kana_answer, correct_answer, answer):
            arr_error.append(44)
        if not helper.check_T10_form_romanji(explain, romanji_answer, correct_answer, answer):
            arr_error.append(45)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.J10(kind_data["audio"]),
            self.L10(kind_data["answer"], kind_data["correct_answer"]),
            self.M10(kind_data["kana_answer"], kind_data["answer"]),
            self.N10(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S10(kind_data["correct_answer"], kind_data["audio"]),
            self.T10(kind_data["explain"], kind_data["audio"], kind_data["correct_answer"],
                     kind_data["kana_answer"], kind_data["romanji_answer"], kind_data["answer"]),
        ]

        return common.flatten_recursive(arr_error)
