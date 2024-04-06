from src.helpers import helper
from src.helpers import common


class Kind_D2_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E2(self, text_question):
        arr_error = []
        if not helper.check_E2_structure_where(text_question):
            arr_error.append(1)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def J2(self, answer):
        arr_error = []
        if not helper.check_J2_has_two_or_four_answers(answer):
            arr_error.append(17)
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        return arr_error

    def K2(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N2(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)
        return arr_error

    def O2(self, explain, answer, correct_answer, romaja_answer, text_question):
        arr_error = []
        if not helper.check_O2_explain_match_answer_and_correct_answer_type_1(explain, answer, correct_answer):
            arr_error.append(48)
        if not helper.check_O2_explain_match_answer_and_romaja_answer_type_1(explain, romaja_answer, correct_answer):
            arr_error.append(49)
        if not helper.check_O2_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(50)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E2(kind_data["text_question"]),
            self.J2(kind_data["answer"]),
            self.K2(kind_data["romaja_answer"], kind_data["answer"]),
            self.N2(kind_data["correct_answer"]),
            self.O2(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["romaja_answer"], kind_data["text_question"])
        ]
        return common.flatten_recursive(arr_error)
