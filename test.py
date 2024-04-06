from src.helpers import common
from src.helpers import helper

print(1111, helper.check_O19_complete_sentences_text_combining_romaja_answer("{{이 보고서는 아주 중요한 것이라서 최선을 다하겠습니다.}}((i bogoseoneun aju jungyohan geosiraseo chweseoneul dahagetsseumnida)) Vì bài báo cáo này rất quan trọng nên tôi sẽ cố gắng hết sức.", "(보고서는)()()()", "i () aju jungyohan () gosiraso () chwesoneul () dahagetsseumnida", "(bogoseoneun)"))