from src.helpers import helper
from src.helpers import common


class Kind_D5_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E5(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(text_question):
            arr_error.append(2)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error


    def F5(self, romaja_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(romaja_question, text_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaja_question):
            arr_error.append(80)
        return arr_error

    def G5(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(12)
        return arr_error

    def H5(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        if not helper.check_H3_like_column(audio, text_question):
            arr_error.append(15)

        return arr_error

    def J5(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J3_has_max_four_answers(answer):
            arr_error.append(19)
        return arr_error

    def K5(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N5(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O5(self, explain, text_question, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O2_explain_match_answer_and_correct_answer_type_1(explain, answer, correct_answer):
            arr_error.append(48)
        if not helper.check_O2_explain_match_answer_and_romaja_answer_type_1(explain, romaja_answer, correct_answer):
            arr_error.append(49)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(58)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def Q3(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_Q3_explain_grammar(explain_grammar, text_question):
            arr_error.append(78)
        if not helper.check_Q3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(79)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E5(kind_data["text_question"]),
            self.F5(kind_data["romaja_question"], kind_data["text_question"]),
            self.G5(kind_data["mean_question"]),
            self.H5(kind_data["audio"], kind_data["text_question"]),
            self.J5(kind_data["answer"]),
            self.K5(kind_data["romaja_answer"], kind_data["answer"]),
            self.N5(kind_data["correct_answer"]),
            self.O5(kind_data["explain"], kind_data["text_question"], kind_data["answer"], 
                    kind_data["correct_answer"], kind_data["romaja_answer"]),
            self.Q3(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
