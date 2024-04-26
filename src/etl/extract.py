import gspread
from google.oauth2.service_account import Credentials
import json
from tqdm import tqdm
import time
from src.helpers import common

# Load credentials from the JSON key file you downloaded
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file(
    'src/configs/google_sheet_api.json', scopes=SCOPES)

GGSHEET_TITLE = 'HeyKorea_Dữ liệu trung cấp'
DATA = 'src/data'


def extract_data():
    client = gspread.authorize(CREDS)

    sheet = client.open(GGSHEET_TITLE)
    worksheets = sheet.worksheets()
    sheet_names = [sheet.title for
                   sheet in worksheets if common.is_number(sheet.title[0]) and (
                       sheet.title == "96_Chế biến món ăn" or 
                       sheet.title == "97_Tiền tệ" or 
                       sheet.title == "98_Ngân hàng" or
                       sheet.title == "99_Tiết kiệm" or 
                       sheet.title == "100_Du lịch (2)"
                    #    sheet.title == "86_Họp mặt" or
                    #    sheet.title == "87_Giúp đỡ" or
                    #    sheet.title == "88_Kết quả" or
                    #    sheet.title == "89_Sức khỏe" or 
                    #    sheet.title == "90_Khuyên nhủ" or 
                    #    sheet.title == "91_Bệnh tật" or 
                    #    sheet.title == "92_Trang phục" or 
                    #    sheet.title == "93_Mua sắm" or 
                    #    sheet.title == "94_Yêu cầu" or 
                    #    sheet.title == "95_Món ăn"
                    )]
    chunk_size = 30
    seperate_sheets = [sheet_names[i:i+chunk_size]
                       for i in range(0, len(sheet_names), chunk_size)]
    for seperate_sheet in seperate_sheets:
        for sheet_name in tqdm(seperate_sheet):
            worksheet_data = sheet.worksheet(sheet_name)
            all_records_worksheet_data = worksheet_data.get_all_records()
            for index, tmp in enumerate(all_records_worksheet_data):
                if (index == 0):
                    continue
                tmp["Unit"] = tmp["Unit"] if bool(
                    tmp["Unit"]) else all_records_worksheet_data[index-1]["Unit"]

            save_data_to_json(all_records_worksheet_data,
                              f'{DATA}/{sheet_name}.json')
    return GGSHEET_TITLE, sheet_names


def save_data_to_json(data, path, type=''):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
