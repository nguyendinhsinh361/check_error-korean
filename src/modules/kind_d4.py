from src.helpers import helper
from src.helpers import common


class Kind_D4_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E4(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(text_question):
            arr_error.append(2)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def F4(self, romaja_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(romaja_question, text_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaja_question):
            arr_error.append(80)
        return arr_error

    def H4(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_korean(audio):
            arr_error.append(13)
        if helper.check_H3_have_tag_p_or_h(audio):
            arr_error.append(14)
        if not helper.check_H3_like_column(audio, text_question):
            arr_error.append(15)

    def J4(self, answer, correct_answer):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(answer):
            arr_error.append(20)
        if not helper.check_J4_contains_enough_words(answer, correct_answer):
            arr_error.append(21)
        if not helper.check_J4_contains_noise_words(answer, correct_answer):
            arr_error.append(22)
        if helper.check_J4_format_sentence(answer):
            arr_error.append(23)
        if helper.check_J4_order_words_diff(answer, correct_answer):
            arr_error.append(24)
        return arr_error

    def N4(self, correct_answer):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(correct_answer):
            arr_error.append(40)
        if not helper.check_J21_muitii_line_breaks(correct_answer):
            arr_error.append(41)
        if not helper.check_N4_pairing_method(correct_answer):
            arr_error.append(42)
        if not helper.check_N4_format_combine_sentences(correct_answer):
            arr_error.append(85)

        return arr_error

    def O4(self, explain, answer, correct_answer, text_question, romaja_question):
        arr_error = []
        if not helper.check_O4_explain_mean_like_text_question_type_2(explain, text_question):
            arr_error.append(51)
        if not helper.check_O4_explain_mean_like_romaja_question_type_2(explain, romaja_question):
            arr_error.append(52)
        if not helper.check_O4_explain_mean_match_correct_answer_type_3(explain, correct_answer):
            arr_error.append(53)
        if not helper.check_O4_count_explain(explain, correct_answer):
            arr_error.append(55)
        if not helper.check_O4_format_combine_sentences(explain):
            arr_error.append(86)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def Q4(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_Q3_explain_grammar(explain_grammar, text_question):
            arr_error.append(78)
        if not helper.check_Q3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(79)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E4(kind_data["text_question"]),
            self.F4(kind_data["romaja_question"], kind_data["text_question"]),
            self.H4(kind_data["audio"], kind_data["text_question"]),
            self.J4(kind_data["answer"], kind_data["correct_answer"]),
            self.N4(kind_data["correct_answer"]),
            self.O4(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["text_question"], kind_data["romaja_question"]),
            self.Q4(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
