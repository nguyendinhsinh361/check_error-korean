from src.helpers import helper
from src.helpers import common


class Kind_D9_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def J9(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        return arr_error

    def L9(self, answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        if not helper.check_L9_audio_contains_answers_accept_dots(answer, audio):
            arr_error.append(18)
        return arr_error

    def M9(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N9(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S9(self, correct_answer, answer, audio):
        arr_error = []
        if not helper.check_S13_type_number_and_like_number_audio(correct_answer, answer, audio):
            arr_error.append(32)
        return arr_error

    def T9(self, explain, audio, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio(explain, audio):
            arr_error.append(46)
        if not helper.check_T2_explain_match_answer_and_kana_answer_type_1(explain, kana_answer, correct_answer):
            arr_error.append(47)
        if not helper.check_T2_explain_match_answer_and_romanji_answer_type_1(explain, romanji_answer, correct_answer):
            arr_error.append(48)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.J9(kind_data["audio"]),
            self.L9(kind_data["answer"], kind_data["audio"]),
            self.M9(kind_data["kana_answer"], kind_data["answer"]),
            self.N9(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S9(kind_data["correct_answer"],
                    kind_data["answer"], kind_data["audio"]),
            self.T9(kind_data["explain"], kind_data["audio"],
                    kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
