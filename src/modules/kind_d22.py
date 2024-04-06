from src.helpers import helper
from src.helpers import common


class Kind_D22_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E22(self, text_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(text_question):
            arr_error.append(6)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def J22(self, answer, correct_answer):
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

    def K22(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N22(self, correct_answer):
        arr_error = []
        if not helper.check_E3_written_by_korean(correct_answer):
            arr_error.append(43)
        if not helper.check_J21_muitii_line_breaks(correct_answer):
            arr_error.append(41)
        if not helper.check_N4_pairing_method(correct_answer):
            arr_error.append(42)
        if not helper.check_N4_format_combine_sentences(correct_answer):
            arr_error.append(85)

        return arr_error

    def O22(self, explain, answer, correct_answer, romaja_answer, text_question):
        arr_error = []
        if not helper.check_O6_match_correct_answer(explain, correct_answer):
            arr_error.append(56)
        # if not helper.check_O6_form_romaja(explain, romaja_answer, correct_answer, answer):
        #     arr_error.append(75)
        if not helper.check_O22_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(76)
        if not helper.check_O4_count_explain(explain, correct_answer):
            arr_error.append(77)
        if not helper.check_O4_format_combine_sentences(explain):
            arr_error.append(86)
        arr_error.append(helper.check_O2_brackets(explain))

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E22(kind_data["text_question"]),
            self.J22(kind_data["answer"], kind_data["correct_answer"]),
            self.K22(kind_data["romaja_answer"], kind_data["answer"]),
            self.N22(kind_data["correct_answer"]),
            self.O22(kind_data["explain"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
