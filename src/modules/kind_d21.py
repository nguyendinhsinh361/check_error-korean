from src.helpers import helper
from src.helpers import common


class Kind_D21_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def L21(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L21_muitii_line_breaks(answer):
            arr_error.append(23)
        if helper.check_L4_format_sentence(answer):
            arr_error.append(24)
        if helper.check_L4_format_sentence(answer):
            arr_error.append(25)
        return arr_error

    def M21(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N21(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S21(self, correct_answer):
        arr_error = []
        if not helper.check_S2_type_number(correct_answer):
            arr_error.append(30)

        return arr_error

    def T21(self, explain, text_question, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T21_complete_sentences_drop_text_combining_correct_answer(explain, correct_answer, answer):
            arr_error.append(34)
        if not helper.check_T21_complete_sentences_drop_text_combining_kana_answer(explain, correct_answer, kana_answer):
            arr_error.append(35)
        if not helper.check_T21_complete_sentences_drop_text_combining_romanji_answer(explain, correct_answer, romanji_answer):
            arr_error.append(36)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.L21(kind_data["answer"]),
            self.M21(kind_data["kana_answer"], kind_data["answer"]),
            self.N21(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S21(kind_data["correct_answer"]),
            self.T21(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
