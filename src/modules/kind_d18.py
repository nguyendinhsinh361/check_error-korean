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
        if not helper.check_E3_written_by_korean(text_question):
            arr_error.append(2)
        if not helper.check_E18_contain_a_pair_of_parentheses(text_question):
            arr_error.append(8)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def F18(self, romaja_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(romaja_question, text_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaja_question):
            arr_error.append(80)
        return arr_error

    def J18(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J3_has_max_four_answers(answer):
            arr_error.append(19)
        return arr_error

    def K18(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error


    def N18(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O18(self, explain, text_question, answer, correct_answer, romaja_answer, romaja_question):
        arr_error = []
        if not helper.check_O18_complete_sentences_answer_combining_correct_answer(explain, correct_answer, text_question, answer):
            arr_error.append(67)
        # if not helper.check_O18_complete_sentences_answer_combining_romaja_answer(explain, correct_answer, romaja_question, romaja_answer):
        #     arr_error.append(68)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(69)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def Q18(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_Q3_explain_grammar(explain_grammar, text_question):
            arr_error.append(78)
        if not helper.check_Q3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(79)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E18(kind_data["text_question"]),
            self.F18(kind_data["romaja_question"], kind_data["text_question"]),
            self.J18(kind_data["answer"]),
            self.K18(kind_data["romaja_answer"], kind_data["answer"]),
            self.N18(kind_data["correct_answer"]),
            self.O18(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"], kind_data["romaja_question"]),
            self.Q18(kind_data["explain_grammar"], kind_data["text_question"]),

        ]
        return common.flatten_recursive(arr_error)
