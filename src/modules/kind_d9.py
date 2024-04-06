from src.helpers import helper
from src.helpers import common


class Kind_D9_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def H9(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        return arr_error

    def J9(self, answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J3_has_max_four_answers(answer):
            arr_error.append(19)
        # if not helper.check_J9_audio_contains_answers_accept_dots(answer, audio):
        #     arr_error.append(23)
        return arr_error

    def K9(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N9(self, correct_answer, answer, audio):
        arr_error = []
        if not helper.check_N13_type_number_and_like_number_audio(correct_answer, answer, audio):
            arr_error.append(44)
        return arr_error

    def O9(self, explain, audio, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O9_explain_like_audio(explain, audio):
            arr_error.append(59)
        if not helper.check_O2_explain_match_answer_and_romaja_answer_type_1(explain, romaja_answer, correct_answer):
            arr_error.append(60)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(58)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.H9(kind_data["audio"]),
            self.J9(kind_data["answer"], kind_data["audio"]),
            self.K9(kind_data["romaja_answer"], kind_data["answer"]),
            self.N9(kind_data["correct_answer"],
                    kind_data["answer"], kind_data["audio"]),
            self.O9(kind_data["explain"], kind_data["audio"],
                    kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
