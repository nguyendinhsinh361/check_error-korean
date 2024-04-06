from src.helpers import helper
from src.helpers import common


class Kind_D16_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def H16(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        return arr_error

    def M16(self, Image_answer):
        arr_error = []
        if not helper.check_M16_two_or_four_img(Image_answer):
            arr_error.append(38)
        return arr_error

    def N16(self, correct_answer):
        arr_error = []
        if not helper.check_N2_type_number(correct_answer):
            arr_error.append(39)

        return arr_error

    def O16(self, explain, audio, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O9_explain_like_audio(explain, audio):
            arr_error.append(59)
        if not helper.check_O15_form_romaja_of_audio(explain, audio):
            arr_error.append(62)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(69)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.H16(kind_data["audio"]),
            self.M16(kind_data["Image_answer"]),
            self.N16(kind_data["correct_answer"]),
            self.O16(kind_data["explain"], kind_data["audio"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
