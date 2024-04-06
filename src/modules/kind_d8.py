from src.helpers import helper
from src.helpers import common


class Kind_D8_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E8(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(text_question):
            arr_error.append(2)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def F8(self, romaja_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(romaja_question, text_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaja_question):
            arr_error.append(80)
        return arr_error

    def G8(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(12)
        return arr_error

    def H8(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        if not helper.check_H3_like_column(audio, text_question):
            arr_error.append(15)

        return arr_error

    def J8(self, answer, correct_answer):
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


    def K8(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error

    def N8(self, correct_answer):
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

    def O8(self, explain, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O6_match_correct_answer(explain, correct_answer):
            arr_error.append(56)
        # if not helper.check_O6_form_romaja(explain, romaja_answer, correct_answer, answer):
        #     arr_error.append(57)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(58)
        if not helper.check_O4_count_explain(explain, correct_answer):
            arr_error.append(55)
        if not helper.check_O4_format_combine_sentences(explain):
            arr_error.append(85)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def Q8(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_Q3_explain_grammar(explain_grammar, text_question):
            arr_error.append(78)
        if not helper.check_Q3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(79)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E8(kind_data["text_question"]),
            self.F8(kind_data["romaja_question"], kind_data["text_question"]),
            self.G8(kind_data["mean_question"]),
            self.H8(kind_data["audio"], kind_data["text_question"]),
            self.J8(kind_data["answer"], kind_data["correct_answer"]),
            self.K8(kind_data["romaja_answer"], kind_data["answer"]),
            self.N8(kind_data["correct_answer"]),
            self.O8(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["romaja_answer"]),
            self.Q8(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
