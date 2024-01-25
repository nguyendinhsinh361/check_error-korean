from src.helpers import helper
from src.helpers import common


class Kind_D12_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E12(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_E12_appear_more_two_han_char(text_question):
            arr_error.append(4)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def F12(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        if not helper.check_format_tag_p(kana_question):
            arr_error.append(110)
        return arr_error

    def G12(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaji_question):
            arr_error.append(111)
        return arr_error

    def H12(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(70)
        return arr_error

    def I12(self, hanviet_question):
        arr_error = []
        if not helper.check_I11_written_by_capital_vietnamese(hanviet_question):
            arr_error.append(77)
        return arr_error

    def J12(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        if not helper.check_J3_like_column(audio, text_question):
            arr_error.append(12)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E12(kind_data["text_question"]),
            self.F12(kind_data["kana_question"], kind_data["text_question"]),
            self.G12(kind_data["romaji_question"], kind_data["kana_question"]),
            self.H12(kind_data["mean_question"]),
            self.H12(kind_data["mean_question"]),
            self.I12(kind_data["hanviet_question"]),
            self.J12(kind_data["audio"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
