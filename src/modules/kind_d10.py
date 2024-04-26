from src.helpers import helper
from src.helpers import common


class Kind_D10_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def H10(self, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        return arr_error

    def J10(self, answer, correct_answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(answer):
            arr_error.append(18)
        if not helper.check_J4_contains_enough_words(answer, correct_answer):
            arr_error.append(21)
        if not helper.check_J4_contains_noise_words(answer, correct_answer):
            arr_error.append(22)
        if helper.check_J4_format_sentence(answer):
            arr_error.append(23)
        if helper.check_J4_order_words_diff(answer, correct_answer):
            arr_error.append(24)
        return arr_error

    def K10(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error


    def N10(self, correct_answer, audio):
        arr_error = []
        if not helper.check_E3_written_by_korean(correct_answer):
            arr_error.append(43)
        if not helper.check_J21_muitii_line_breaks(correct_answer):
            arr_error.append(41)
        if not helper.check_N10_like_audio_question(correct_answer, audio):
            arr_error.append(45)
        return arr_error

    def O10(self, explain, audio, correct_answer, romaja_answer, answer):
        arr_error = []
        if not helper.check_O9_explain_like_audio(explain, audio):
            arr_error.append(59)
        if not helper.check_O10_form_romaja(explain, romaja_answer, correct_answer, answer):
            arr_error.append(57)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(58)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.H10(kind_data["audio"]),
            self.J10(kind_data["answer"], kind_data["correct_answer"]),
            self.K10(kind_data["romaja_answer"], kind_data["answer"]),
            self.N10(kind_data["correct_answer"], kind_data["audio"]),
            self.O10(kind_data["explain"], kind_data["audio"], kind_data["correct_answer"],
                     kind_data["romaja_answer"], kind_data["answer"]),
        ]

        return common.flatten_recursive(arr_error)
