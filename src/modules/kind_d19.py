from src.helpers import helper
from src.helpers import common


class Kind_D19_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E19(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(text_question):
            arr_error.append(2)
        if not helper.check_E19_contain_more_pair_of_parentheses(text_question):
            arr_error.append(9)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def F19(self, romaja_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(romaja_question, text_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaja_question):
            arr_error.append(80)
        return arr_error


    def J19(self, answer):
        arr_error = []
        if not helper.check_J19_structure_pair_of_parentheses(answer):
            arr_error.append(32)
        return arr_error

    def K19(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N19(self, correct_answer, answer):
        arr_error = []
        if not helper.check_N19_correct_answer_has_pair_of_parentheses_and_like_answer(correct_answer, answer):
            arr_error.append(47)

        return arr_error

    def O19(self, explain, text_question, answer, correct_answer, romaja_answer, romaja_question):
        arr_error = []
        if not helper.check_O19_complete_sentences_text_combining_correct_answer(explain, correct_answer, text_question, answer):
            arr_error.append(70)
        # if not helper.check_O19_complete_sentences_text_combining_romaja_answer(explain, correct_answer, romaja_question, romaja_answer):
        #     arr_error.append(71)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(69)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def Q19(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_Q3_explain_grammar(explain_grammar, text_question):
            arr_error.append(78)
        if not helper.check_Q3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(79)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E19(kind_data["text_question"]),
            self.F19(kind_data["romaja_question"], kind_data["text_question"]),
            self.J19(kind_data["answer"]),
            self.K19(kind_data["romaja_answer"], kind_data["answer"]),
            self.N19(kind_data["correct_answer"], kind_data["answer"]),
            self.O19(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"], kind_data["romaja_question"]),
            self.Q19(kind_data["explain_grammar"], kind_data["text_question"]),

        ]
        return common.flatten_recursive(arr_error)
