from src.helpers import helper
from src.helpers import common


class Kind_D20_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E20(self, text_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(text_question):
            arr_error.append(6)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def J20(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J3_has_max_four_answers(answer):
            arr_error.append(19)
        return arr_error

    def K20(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N20(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O20(self, explain, text_question, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O2_explain_match_answer_and_correct_answer_type_1(explain, answer, correct_answer):
            arr_error.append(48)
        if not helper.check_O2_explain_match_answer_and_romaja_answer_type_1(explain, romaja_answer, correct_answer):
            arr_error.append(49)
        if not helper.check_O13_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(72)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E20(kind_data["text_question"]),
            self.J20(kind_data["answer"]),
            self.K20(kind_data["romaja_answer"], kind_data["answer"]),
            self.N20(kind_data["correct_answer"]),
            self.O20(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
