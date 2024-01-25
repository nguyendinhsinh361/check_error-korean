from src.helpers import common

def check_E3_written_by_korean(text):
    text = text.strip("\n")
    if (not text):
        return False
    clean_text = common.get_text_from_html(text)
    return any(common.is_korean(element) for element in clean_text)




