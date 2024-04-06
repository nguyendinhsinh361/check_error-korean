from src.helpers import helper
from src.helpers import common


class Kind_D17_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E17(self, text_question):
        arr_error = []
        if not helper.check_E17_structure_translate(text_question):
            arr_error.append(7)
        if not helper.check_E3_has_tag_p_same(text_question):
            arr_error.append(3)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(80)
        return arr_error

    def I17(self, image):
        arr_error = []
        if not helper.check_I17_has_content(image):
            arr_error.append(16)
        return arr_error

    def J17(self, answer, correct_answer):
        arr_error = []
        if not helper.check_J17_count_korean_words(answer):
            arr_error.append(27)
        if not helper.check_J4_contains_enough_words(answer, correct_answer):
            arr_error.append(28)
        if not helper.check_J4_contains_noise_words(answer, correct_answer):
            arr_error.append(29)
        if not helper.check_J17_has_punctuation(answer):
            arr_error.append(30)
        if helper.check_J4_order_words_diff(answer, correct_answer):
            arr_error.append(24)
        return arr_error

    def K17(self, romaja_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(romaja_answer, answer):
            arr_error.append(36)
        return arr_error


    def N17(self, correct_answer):
        arr_error = []
        if not helper.check_J17_count_korean_words(correct_answer):
            arr_error.append(46)

        return arr_error

    def O17(self, explain, text_question, answer, correct_answer, romaja_answer):
        arr_error = []
        if not helper.check_O17_expression_kanji_of_correct_answer(explain, correct_answer):
            arr_error.append(64)
        if not helper.check_O6_match_correct_answer(explain, correct_answer):
            arr_error.append(54)
        if not helper.check_O5_check_mean_vietnamese(explain):
            arr_error.append(69)
        if not helper.check_O2_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(66)
        arr_error.append(helper.check_O2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E17(kind_data["text_question"]),
            self.I17(kind_data["image"]),
            self.J17(kind_data["answer"], kind_data["correct_answer"]),
            self.K17(kind_data["romaja_answer"], kind_data["answer"]),
            self.N17(kind_data["correct_answer"]),
            self.O17(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["correct_answer"], kind_data["romaja_answer"]),
        ]
        return common.flatten_recursive(arr_error)
