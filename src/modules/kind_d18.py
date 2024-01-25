from src.helpers import helper
from src.helpers import common


class Kind_D18_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E18(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E18_contain_a_pair_of_parentheses(text_question):
            arr_error.append(7)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def F18(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        if not helper.check_format_tag_p(kana_question):
            arr_error.append(110)
        return arr_error

    def G18(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaji_question):
            arr_error.append(111)
        return arr_error

    def L18(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        return arr_error

    def M18(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N18(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S18(self, correct_answer):
        arr_error = []
        if not helper.check_S2_type_number(correct_answer):
            arr_error.append(30)

        return arr_error

    def T18(self, explain, text_question, answer, correct_answer, kana_answer, romanji_answer, kana_question, romanji_question):
        arr_error = []
        if not helper.check_T18_complete_sentences_answer_combining_correct_answer(explain, correct_answer, text_question, answer):
            arr_error.append(57)
        if not helper.check_T18_complete_sentences_answer_combining_kana_answer(explain, correct_answer, kana_question, kana_answer):
            arr_error.append(58)
        if not helper.check_T18_complete_sentences_answer_combining_romanji_answer(explain, correct_answer, romanji_question, romanji_answer):
            arr_error.append(59)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def V18(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E18(kind_data["text_question"]),
            self.F18(kind_data["kana_question"], kind_data["text_question"]),
            self.G18(kind_data["romaji_question"], kind_data["kana_question"]),
            self.L18(kind_data["answer"]),
            self.M18(kind_data["kana_answer"], kind_data["answer"]),
            self.N18(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S18(kind_data["correct_answer"]),
            self.T18(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["kana_answer"], kind_data["romanji_answer"], kind_data["kana_question"], kind_data["romaji_question"]),
            self.V18(kind_data["explain_grammar"], kind_data["text_question"]),

        ]
        return common.flatten_recursive(arr_error)
