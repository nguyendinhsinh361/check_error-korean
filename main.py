
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
#     helper.check_J4_contains_enough_words("""ngay khi
# gọi bạn
# nhắn tin
# về đến
# nhà
# tôi sẽ""", """tôi sẽ
# gọi bạn
# ngay khi
# về đến
# nhà
# ###
# ngay khi
# về đến
# nhà
# tôi sẽ
# gọi bạn""")
    return 1

if __name__ == "__main__":
    main()
