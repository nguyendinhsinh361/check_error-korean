from src.etl import extract
from src.etl import transform
import os
DATA_ERROR_EXCEL = 'src/excel'


def etl_stream():
    GGSHEET_TITLE, paths_data = extract.extract_data()
    try:
        os.remove(f'{DATA_ERROR_EXCEL}/Check Error {GGSHEET_TITLE}.xlsx')
    except OSError as e:
        print(e)
    for path_data in paths_data:
        transform.transform_stream(GGSHEET_TITLE, path_data)
