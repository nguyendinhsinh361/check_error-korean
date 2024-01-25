from src.helpers import helper
from src.helpers import common


class Kind_D13_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E13(self, text_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(text_question):
            arr_error.append(5)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def J13(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        return arr_error

    def L13(self, answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        if not helper.check_L13_audio_contains_answers(answer, audio):
            arr_error.append(19)
        return arr_error

    def M13(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N13(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S13(self, correct_answer, answer, audio):
        arr_error = []
        if not helper.check_S13_type_number_and_like_number_audio(correct_answer, answer, audio):
            arr_error.append(32)
        return arr_error

    def T13(self, explain, text_question, audio, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio(explain, audio):
            arr_error.append(46)
        if not helper.check_T2_explain_match_answer_and_kana_answer_type_1(explain, kana_answer, correct_answer):
            arr_error.append(47)
        if not helper.check_T2_explain_match_answer_and_romanji_answer_type_1(explain, romanji_answer, correct_answer):
            arr_error.append(48)
        if not helper.check_T13_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(86)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E13(kind_data["text_question"]),
            self.J13(kind_data["audio"]),
            self.L13(kind_data["answer"], kind_data["audio"]),
            self.M13(kind_data["kana_answer"], kind_data["answer"]),
            self.N13(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S13(kind_data["correct_answer"],
                     kind_data["answer"], kind_data["audio"]),
            self.T13(kind_data["explain"], kind_data["text_question"], kind_data["audio"],
                     kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
