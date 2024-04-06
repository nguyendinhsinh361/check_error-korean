
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
#     helper.check_J4_contains_enough_words("""가
# 신입생이
# 민호
# 입니다
# 씨
# 민준
# 아닙니다
# 씨
# 신입생
# 가""", """민호
# 씨
# 가
# 신입생이
# 아닙니다
# 민준
# 씨
# 가
# 신입생
# 입니다""")
    return 1

if __name__ == "__main__":
    main()
