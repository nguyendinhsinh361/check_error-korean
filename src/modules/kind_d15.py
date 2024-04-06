from src.helpers import helper
from src.helpers import common


class Kind_D15_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def H15(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        return arr_error

    def J15(self, answer):
        
        arr_error = []
        if not helper.check_J3_has_max_four_answers(answer):
            arr_error.append(19)
        if not helper.check_E13_written_by_vietnamese(answer):            
            arr_error.append(20)

        return arr_error

    def N15(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O15(self, explain, audio, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O9_explain_like_audio(explain, audio):
            arr_error.append(59)
        if not helper.check_O15_form_romaja_of_audio(explain, audio):
            arr_error.append(62)
        if not helper.check_O3_explain_mean_match_correct_answer_type_2(explain, answer, correct_answer):
            arr_error.append(63)
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.H15(kind_data["audio"]),
            self.J15(kind_data["answer"]),
            self.N15(kind_data["correct_answer"]),
            self.O15(kind_data["explain"], kind_data["audio"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
