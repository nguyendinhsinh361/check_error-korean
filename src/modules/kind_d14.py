from src.helpers import helper
from src.helpers import common


class Kind_D14_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E14(self, text_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(text_question):
            arr_error.append(5)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def J14(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        return arr_error

    def L14(self, answer, correct_answer):
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

    def M14(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N14(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S14(self, correct_answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(correct_answer):
            arr_error.append(72)
        if not helper.check_L21_muitii_line_breaks(correct_answer):
            arr_error.append(75)
        if not helper.check_S14_correct_answer_like_audio(correct_answer, audio):
            arr_error.append(33)
        return arr_error

    def T14(self, explain, text_question, audio, correct_answer, kana_answer, romanji_answer, answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio(explain, audio):
            arr_error.append(46)
        if not helper.check_T10_form_kana(explain, kana_answer, correct_answer, answer):
            arr_error.append(44)
        if not helper.check_T10_form_romanji(explain, romanji_answer, correct_answer, answer):
            arr_error.append(45)
        if not helper.check_T13_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(86)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E14(kind_data["text_question"]),
            self.J14(kind_data["audio"]),
            self.L14(kind_data["answer"], kind_data["correct_answer"]),
            self.M14(kind_data["kana_answer"], kind_data["answer"]),
            self.N14(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S14(kind_data["correct_answer"], kind_data["audio"]),
            self.T14(kind_data["explain"], kind_data["text_question"], kind_data["audio"], kind_data["correct_answer"],
                     kind_data["kana_answer"], kind_data["romanji_answer"], kind_data["answer"]),
        ]
        return common.flatten_recursive(arr_error)
