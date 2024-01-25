from src.helpers import helper
from src.helpers import common


class Kind_D3_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E3(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def F3(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        if not helper.check_format_tag_p(kana_question):
            arr_error.append(110)
        return arr_error

    def G3(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaji_question):
            arr_error.append(111)
        return arr_error

    def J3(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        if not helper.check_J3_like_column(audio, text_question):
            arr_error.append(12)

        return arr_error

    def L3(self, answer):
        arr_error = []
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        if not helper.check_E13_written_by_vietnamese(answer):
            arr_error.append(73)

        return arr_error

    def S3(self, correct_answer):
        arr_error = []
        if not helper.check_S2_type_number(correct_answer):
            arr_error.append(30)

        return arr_error

    def T3(self, explain, answer, correct_answer, text_question, kana_question, romanji_question):
        arr_error = []
        if not helper.check_T3_explain_mean_like_text_question_type_2(explain, text_question):
            arr_error.append(86)
        if not helper.check_T3_explain_mean_like_kana_question_type_2(explain, kana_question):
            arr_error.append(38)
        if not helper.check_T3_explain_mean_like_romanji_question_type_2(explain, romanji_question):
            arr_error.append(39)
        if not helper.check_T3_explain_mean_match_correct_answer_type_2(explain, answer, correct_answer):
            arr_error.append(40)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def V3(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E3(kind_data["text_question"]),
            self.F3(kind_data["kana_question"], kind_data["text_question"]),
            self.G3(kind_data["romaji_question"], kind_data["kana_question"]),
            self.J3(kind_data["audio"], kind_data["text_question"]),
            self.L3(kind_data["answer"]),
            self.S3(kind_data["correct_answer"]),
            self.T3(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["text_question"], kind_data["kana_question"], kind_data["romaji_question"]),
            self.V3(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
