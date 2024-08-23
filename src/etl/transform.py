from src.enums.kind import Kind
from src.modules.kind_d2 import Kind_D2_Service
from src.modules.kind_d3 import Kind_D3_Service
from src.modules.kind_d4 import Kind_D4_Service
from src.modules.kind_d5 import Kind_D5_Service
from src.modules.kind_d6 import Kind_D6_Service
from src.modules.kind_d7 import Kind_D7_Service
from src.modules.kind_d8 import Kind_D8_Service
from src.modules.kind_d9 import Kind_D9_Service
from src.modules.kind_d10 import Kind_D10_Service
from src.modules.kind_d11 import Kind_D11_Service
from src.modules.kind_d12 import Kind_D12_Service
from src.modules.kind_d13 import Kind_D13_Service
from src.modules.kind_d14 import Kind_D14_Service
from src.modules.kind_d15 import Kind_D15_Service
from src.modules.kind_d16 import Kind_D16_Service
from src.modules.kind_d17 import Kind_D17_Service
from src.modules.kind_d18 import Kind_D18_Service
from src.modules.kind_d19 import Kind_D19_Service
from src.modules.kind_d20 import Kind_D20_Service
from src.modules.kind_d21 import Kind_D21_Service
from src.modules.kind_d22 import Kind_D22_Service
from src.modules.kind_d23 import Kind_D23_Service
from src.modules.kind_d24 import Kind_D24_Service
from src.helpers import common, helper
from tqdm import tqdm

DATA = 'src/data'
DATA_ERROR = 'src/error'
DATA_ERROR_EXCEL = 'src/excel'
DATA_RULE = 'src/static/korea_rule.json'


def transform_stream(GGSHEET_TITLE, path_data):
    kind_data = common.get_raw_data(f'{DATA}/{path_data}.json')
    count_questions_check_data = [item["Count questions "] for item in kind_data if item["Count questions "]]
    lesson_check = kind_data[0]["Lesson "] if "Lesson " in kind_data[0] else kind_data[0]["Lesson"]
    
    count_questions_check = helper.check_arrays(count_questions_check_data)
    result_error = {}

    if(not count_questions_check):
        result_error["count_questions_check"] = {
            "kind": "All",
            "unit": "All",
            "count_questions": "All",
            "text_question": "All",
            "error": [90]
        }
    if(not lesson_check == path_data.split("_")[1]):
        result_error["count_questions_check"] = {
            "kind": "All",
            "unit": "All",
            "count_questions": "All",
            "text_question": "All",
            "error": [91]
        }
    for data in tqdm(kind_data):
        # if (data["kind"].strip() == (Kind.KIND_15.value).strip()):
        #     kind_d15 = Kind_D15_Service(data)
        #     result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
        #         "kind": data["kind"],
        #         "unit": data["Unit"],
        #         "count_questions": data["Count questions "],
        #         "text_question": data["text_question"],
        #         "error": kind_d15.run()
        #     }
        if (data["kind"].strip() == (Kind.KIND_2.value).strip()):
            kind_d2 = Kind_D2_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d2.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_3.value).strip()):
            kind_d3 = Kind_D3_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d3.run()
            }

        if (data["kind"].strip() == (Kind.KIND_4.value).strip()):
            kind_d4 = Kind_D4_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d4.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_5.value).strip()):
            kind_d5 = Kind_D5_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d5.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_6.value).strip()):
            kind_d6 = Kind_D6_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d6.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_7.value).strip()):
            kind_d7 = Kind_D7_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d7.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_8.value).strip()):
            kind_d8 = Kind_D8_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d8.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_9.value).strip()):
            kind_d9 = Kind_D9_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d9.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_10.value).strip()):
            kind_d10 = Kind_D10_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d10.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_11.value).strip()):
            kind_d11 = Kind_D11_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d11.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_12.value).strip()):
            kind_d12 = Kind_D12_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d12.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_13.value).strip()):
            kind_d13 = Kind_D13_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d13.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_14.value).strip()):
            kind_d14 = Kind_D14_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d14.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_15.value).strip()):
            kind_d15 = Kind_D15_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d15.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_16.value).strip()):
            kind_d16 = Kind_D16_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d16.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_17.value).strip()):
            kind_d17 = Kind_D17_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d17.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_18.value).strip()):
            kind_d18 = Kind_D18_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d18.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_19.value).strip()):
            kind_d19 = Kind_D19_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d19.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_20.value).strip()):
            kind_d20 = Kind_D20_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d20.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_21.value).strip()):
            kind_d21 = Kind_D21_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d21.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_22.value).strip()):
            kind_d22 = Kind_D22_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d22.run()
            }
        elif (data["kind"].strip() == (Kind.KIND_23.value).strip()):
            kind_d22 = Kind_D23_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d22.run()
            }
        elif (data["kind"].strip() == (Kind.KIND_24.value).strip()):
            kind_d22 = Kind_D24_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}, unit: {data["Unit"]}'] = {
                "kind": data["kind"],
                "unit": data["Unit"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d22.run()
            }

    result_completed_raw = []
    result_completed = []
    for value in result_error.values():
        result_completed_raw.append(value)
    rule_data = common.get_raw_data(DATA_RULE)
    for index, tmp in enumerate(result_completed_raw):
        error_values = tmp.get("error", [])
        column = ""
        for data in error_values:
            try:
                column += "- " + (rule_data[str(data)]["column"]).lstrip() + \
                    ": " + (rule_data[str(data)]["content"]).lstrip() + "\n"
            except Exception as e:
                print(data)
        result_completed.append(
            {"kind": tmp["kind"], "unit": tmp["unit"] if bool(tmp["unit"].strip()) else result_completed[index-1]["unit"], "count_questions": tmp["count_questions"], "content": column})

    result_completed = common.flatten_recursive(result_completed)
    result_completed = [tmp for tmp in result_completed if len(
        tmp["content"].split("\n")) > 1]
    common.save_data_to_json(
        result_completed, f'{DATA_ERROR}/{path_data}.json')
    common.add_sheet_pandas(f'{DATA_ERROR_EXCEL}/Check Error {GGSHEET_TITLE}.xlsx',
                            path_data, result_completed)
    # return result_error
    # extract.extract_data()
