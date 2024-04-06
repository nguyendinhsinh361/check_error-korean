from src.helpers import helper
from src.helpers import common


class Kind_D21_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def J21(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J21_muitii_line_breaks(answer):
            arr_error.append(33)
        if helper.check_J4_format_sentence(answer):
            arr_error.append(34)
        if helper.check_J4_format_sentence(answer):
            arr_error.append(35)
        return arr_error

    def K21(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error


    def N21(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O21(self, explain, text_question, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O21_complete_sentences_drop_text_combining_correct_answer(explain, correct_answer, answer):
            arr_error.append(73)
        # if not helper.check_O21_complete_sentences_drop_text_combining_romaja_answer(explain, correct_answer, romaja_answer):
        #     arr_error.append(74)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(69)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.J21(kind_data["answer"]),
            self.K21(kind_data["romaja_answer"], kind_data["answer"]),
            self.N21(kind_data["correct_answer"]),
            self.O21(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
