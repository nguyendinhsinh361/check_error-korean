
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
    # helper.check_J4_contains_enough_words("b\nb\nb\nb\nb\nb\nb", "b\nc")
    return 1

if __name__ == "__main__":
    main()
