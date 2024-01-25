
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
    # helper.check_T15_form_romanji_of_audio("{{私を愛してるの？}}[[わたしをあいしてるの？]]((Watashi o aishiteruno?)) Anh có yêu em không?", "1111")


if __name__ == "__main__":
    main()
